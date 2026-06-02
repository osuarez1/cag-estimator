"""End-to-end verification for the CAG estimator service.

This script is designed to be runnable locally and in CI.
It validates:
- server starts
- GET /health returns 200
- GET /docs returns 200
- POST /api/v1/estimate returns an estimation influenced by context examples
- .env is gitignored
"""

from __future__ import annotations

import json
import os
import signal
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

_DEBUG_LOG = Path(__file__).resolve().parents[1] / ".cursor" / "debug-89ab8e.log"


def _dbg(hypothesis_id: str, location: str, message: str, data: dict | None = None) -> None:
    # region agent log
    import json as _json

    payload = {
        "sessionId": "89ab8e",
        "runId": os.environ.get("VERIFY_DEBUG_RUN_ID", "pre-fix"),
        "hypothesisId": hypothesis_id,
        "location": location,
        "message": message,
        "data": data or {},
        "timestamp": int(time.time() * 1000),
    }
    _DEBUG_LOG.parent.mkdir(parents=True, exist_ok=True)
    with _DEBUG_LOG.open("a", encoding="utf-8") as f:
        f.write(_json.dumps(payload) + "\n")
    # endregion


def _http_json(method: str, url: str, body: dict | None = None) -> tuple[int, dict]:
    data = None
    headers = {}
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            raw = resp.read().decode("utf-8")
            return resp.status, json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8") if e.fp else ""
        try:
            payload = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            payload = {"raw": raw}
        return e.code, payload


def _http_text(method: str, url: str) -> int:
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req, timeout=5) as resp:
        _ = resp.read()
        return resp.status


def _assert(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def _log(msg: str) -> None:
    print(msg, flush=True)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    _dbg("H1", "verify.py:main", "main_entered", {"repo_root": str(repo_root)})
    _log("Running estimador-cag verification...")

    gitignore = (repo_root / ".gitignore").read_text(encoding="utf-8")
    _assert("\n.env\n" in f"\n{gitignore}\n", "Expected `.env` to be listed in .gitignore")
    _dbg("H1", "verify.py:main", "gitignore_ok")
    _log("  [ok] .env is listed in .gitignore")

    transcript_path = repo_root / "exercises" / "transcripts" / "meeting_transcript.md"
    transcript = transcript_path.read_text(encoding="utf-8").strip()
    _assert(len(transcript) > 0, "Transcript file is empty")
    _dbg("H3", "verify.py:main", "transcript_loaded", {"chars": len(transcript)})
    _log(f"  [ok] loaded transcript ({len(transcript)} chars)")

    host = os.environ.get("VERIFY_HOST", "127.0.0.1")
    port = int(os.environ.get("VERIFY_PORT", "8001"))
    base_url = f"http://{host}:{port}"

    env = os.environ.copy()
    env.setdefault("LLM_PROVIDER", "mock")
    _dbg("H2", "verify.py:main", "server_config", {"host": host, "port": port, "llm_provider": env.get("LLM_PROVIDER")})
    _log(f"  starting server at {base_url} (LLM_PROVIDER={env.get('LLM_PROVIDER')})...")

    cmd = [
        sys.executable,
        "-m",
        "uvicorn",
        "app.main:app",
        "--host",
        host,
        "--port",
        str(port),
        "--log-level",
        "warning",
    ]

    proc = subprocess.Popen(
        cmd,
        cwd=str(repo_root),
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )

    try:
        # Wait for readiness
        deadline = time.time() + 20
        last_err: str | None = None
        while time.time() < deadline:
            try:
                status, payload = _http_json("GET", f"{base_url}/health")
                if status == 200 and payload.get("status") == "ok":
                    _dbg("H3", "verify.py:main", "health_ok", {"status": status})
                    _log("  [ok] GET /health")
                    break
                last_err = f"unexpected health response: {status} {payload}"
            except Exception as e:  # noqa: BLE001 - startup polling
                last_err = str(e)
            time.sleep(0.25)
        else:
            out = proc.stdout.read() if proc.stdout else ""
            raise RuntimeError(f"Server did not become ready: {last_err}\n{out}")

        docs_status = _http_text("GET", f"{base_url}/docs")
        _assert(docs_status == 200, "Expected /docs to return 200")
        _dbg("H3", "verify.py:main", "docs_ok", {"status": docs_status})
        _log("  [ok] GET /docs")

        status, payload = _http_json(
            "POST",
            f"{base_url}/api/v1/estimate",
            {"transcription": transcript},
        )
        _assert(status == 200, f"Expected 200 from /api/v1/estimate, got {status}: {payload}")
        estimation = payload.get("estimation", "")
        _assert(isinstance(estimation, str) and estimation.strip(), "Expected non-empty `estimation`")

        # Context-inspired markers (present in historical examples)
        _assert("### Task Breakdown" in estimation, "Expected `### Task Breakdown` in estimation")
        _assert("**Total estimated" in estimation, "Expected `**Total estimated` marker in estimation")
        _assert("**Recommended team:**" in estimation, "Expected `**Recommended team:**` marker in estimation")
        _dbg(
            "H1",
            "verify.py:main",
            "all_checks_passed",
            {"estimate_status": status, "estimation_len": len(estimation)},
        )
        _log(f"  [ok] POST /api/v1/estimate ({len(estimation)} chars)")
        _log("All verification checks passed.")

        return 0
    finally:
        if proc.poll() is None:
            proc.send_signal(signal.SIGTERM)
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.wait(timeout=5)


if __name__ == "__main__":
    raise SystemExit(main())

