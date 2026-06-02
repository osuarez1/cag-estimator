"""Run POST /api/v1/estimate against each LLM provider and write Markdown reports.

Starts uvicorn once per provider (LLM_PROVIDER must be set at process start).
Writes one report per provider under reports/providers/.
"""

from __future__ import annotations

import argparse
import json
import os
import signal
import subprocess
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from app.services.llm_service import _DEFAULT_MODELS as PROVIDER_DEFAULT_MODELS

PROVIDERS = tuple(PROVIDER_DEFAULT_MODELS.keys())
DEFAULT_TRANSCRIPT = Path("exercises/transcripts/meeting_transcript.md")
DEFAULT_REPORTS_DIR = Path("reports/providers")
DEFAULT_HOST = "127.0.0.1"
DEFAULT_BASE_PORT = 8100
STARTUP_TIMEOUT_S = 25
REQUEST_TIMEOUT_S = 120


@dataclass
class TranscriptionInput:
    text: str
    source_label: str


@dataclass
class ProviderRunResult:
    provider: str
    base_url: str
    http_status: int
    payload: dict
    startup_s: float
    request_s: float
    error: str | None = None


def _http_json(
    method: str,
    url: str,
    body: dict | None = None,
    *,
    timeout_s: float = REQUEST_TIMEOUT_S,
) -> tuple[int, dict]:
    data = None
    headers: dict[str, str] = {}
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout_s) as resp:
            raw = resp.read().decode("utf-8")
            return resp.status, json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8") if e.fp else ""
        try:
            payload = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            payload = {"raw": raw}
        return e.code, payload


def _log(msg: str) -> None:
    print(msg, flush=True)


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Test all LLM providers via the estimate API and write Markdown reports.",
    )
    parser.add_argument(
        "--transcription-file",
        type=Path,
        help="Path to a transcript file (UTF-8). Mutually exclusive with --transcription.",
    )
    parser.add_argument(
        "--transcription",
        help="Inline transcript text. Mutually exclusive with --transcription-file.",
    )
    parser.add_argument(
        "--reports-dir",
        type=Path,
        default=DEFAULT_REPORTS_DIR,
        help=f"Output directory for reports (default: {DEFAULT_REPORTS_DIR})",
    )
    parser.add_argument(
        "--host",
        default=os.environ.get("TEST_PROVIDERS_HOST", DEFAULT_HOST),
        help=f"Server bind host (default: {DEFAULT_HOST})",
    )
    parser.add_argument(
        "--base-port",
        type=int,
        default=int(os.environ.get("TEST_PROVIDERS_BASE_PORT", str(DEFAULT_BASE_PORT))),
        help=f"Base port; each provider uses base_port + index (default: {DEFAULT_BASE_PORT})",
    )
    return parser.parse_args(argv)


def _load_transcription(args: argparse.Namespace, repo_root: Path) -> TranscriptionInput:
    if args.transcription_file is not None and args.transcription is not None:
        raise SystemExit("Use only one of --transcription-file or --transcription.")

    if args.transcription_file is not None:
        path = args.transcription_file if args.transcription_file.is_absolute() else repo_root / args.transcription_file
        if not path.is_file():
            raise SystemExit(f"Transcription file not found: {path}")
        text = path.read_text(encoding="utf-8").strip()
        return TranscriptionInput(text=text, source_label=str(path.relative_to(repo_root)))

    if args.transcription is not None:
        text = args.transcription.strip()
        return TranscriptionInput(text=text, source_label="inline")

    default_path = repo_root / DEFAULT_TRANSCRIPT
    if not default_path.is_file():
        raise SystemExit(f"Default transcript not found: {default_path}")
    text = default_path.read_text(encoding="utf-8").strip()
    return TranscriptionInput(text=text, source_label=str(DEFAULT_TRANSCRIPT))


def _wait_for_health(base_url: str, deadline: float) -> tuple[bool, str | None]:
    last_err: str | None = None
    while time.time() < deadline:
        try:
            status, payload = _http_json("GET", f"{base_url}/health", timeout_s=5)
            if status == 200 and payload.get("status") == "ok":
                return True, None
            last_err = f"unexpected health response: {status} {payload}"
        except Exception as e:  # noqa: BLE001 - startup polling
            last_err = str(e)
        time.sleep(0.25)
    return False, last_err


def _run_provider(
    *,
    repo_root: Path,
    provider: str,
    port: int,
    host: str,
    transcription: str,
    env_base: dict[str, str],
) -> ProviderRunResult:
    base_url = f"http://{host}:{port}"
    env = env_base.copy()
    env["LLM_PROVIDER"] = provider
    # Force provider-specific model so a global LLM_MODEL / .env value (e.g. gpt-4o-mini)
    # is not sent to Anthropic or Gemini.
    env["LLM_MODEL"] = PROVIDER_DEFAULT_MODELS[provider]

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

    t0 = time.perf_counter()
    try:
        ready, last_err = _wait_for_health(base_url, time.time() + STARTUP_TIMEOUT_S)
        startup_s = time.perf_counter() - t0
        if not ready:
            out = proc.stdout.read() if proc.stdout else ""
            return ProviderRunResult(
                provider=provider,
                base_url=base_url,
                http_status=0,
                payload={},
                startup_s=startup_s,
                request_s=0.0,
                error=f"Server did not become ready: {last_err}\n{out}",
            )

        t_req = time.perf_counter()
        status, payload = _http_json(
            "POST",
            f"{base_url}/api/v1/estimate",
            {"transcription": transcription},
        )
        request_s = time.perf_counter() - t_req
        return ProviderRunResult(
            provider=provider,
            base_url=base_url,
            http_status=status,
            payload=payload,
            startup_s=startup_s,
            request_s=request_s,
        )
    finally:
        if proc.poll() is None:
            proc.send_signal(signal.SIGTERM)
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.wait(timeout=5)


def _format_report(
    result: ProviderRunResult,
    *,
    transcription_source: str,
    transcription_chars: int,
    generated_at: datetime,
) -> str:
    lines: list[str] = [
        f"## Provider run: {result.provider}",
        "",
        "### Metadata",
        "",
        f"- **Generated at:** {generated_at.isoformat()}",
        f"- **Provider:** `{result.provider}`",
        f"- **Base URL:** `{result.base_url}`",
        f"- **HTTP status:** {result.http_status}",
        f"- **Startup time:** {result.startup_s:.2f}s",
        f"- **Request time:** {result.request_s:.2f}s",
        f"- **Transcription source:** `{transcription_source}`",
        f"- **Transcription length:** {transcription_chars} characters",
        "",
    ]

    if result.error:
        lines.extend(["### Error", "", "```", result.error.strip(), "```", ""])
        return "\n".join(lines)

    if result.http_status == 200:
        model = result.payload.get("model", "")
        lines.append(f"- **Model:** `{model}`")
        usage_bits: list[str] = []
        for key in ("input_tokens", "output_tokens", "thinking_tokens"):
            val = result.payload.get(key)
            if val is not None:
                usage_bits.append(f"{key}={val}")
        if usage_bits:
            lines.append(f"- **Usage:** {', '.join(usage_bits)}")
        if "cost_usd" in result.payload:
            lines.append(f"- **Cost (USD):** {result.payload['cost_usd']}")
        lines.append("")

        estimation = result.payload.get("estimation", "")
        if isinstance(estimation, str) and estimation.strip():
            lines.extend(["### Estimation", "", estimation.strip(), ""])
        else:
            lines.extend(["### Estimation", "", "_Empty estimation in response._", ""])
    else:
        detail = result.payload.get("detail", result.payload)
        lines.extend(
            [
                "### API error",
                "",
                "```json",
                json.dumps(detail, indent=2, ensure_ascii=False),
                "```",
                "",
            ]
        )

    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    repo_root = Path(__file__).resolve().parents[1]
    transcription_input = _load_transcription(args, repo_root)

    if not transcription_input.text:
        raise SystemExit("Transcription is empty.")

    reports_dir = args.reports_dir if args.reports_dir.is_absolute() else repo_root / args.reports_dir
    reports_dir.mkdir(parents=True, exist_ok=True)

    env_base = os.environ.copy()
    generated_at = datetime.now(timezone.utc)

    _log(
        f"Testing {len(PROVIDERS)} providers; transcription from {transcription_input.source_label} "
        f"({len(transcription_input.text)} chars)"
    )
    _log(f"Writing reports to {reports_dir}")

    failures = 0
    for index, provider in enumerate(PROVIDERS):
        port = args.base_port + index
        model = PROVIDER_DEFAULT_MODELS[provider]
        _log(f"\n[{provider}] starting server on port {port} (LLM_MODEL={model})...")
        result = _run_provider(
            repo_root=repo_root,
            provider=provider,
            port=port,
            host=args.host,
            transcription=transcription_input.text,
            env_base=env_base,
        )

        report_path = reports_dir / f"{provider}.md"
        report_body = _format_report(
            result,
            transcription_source=transcription_input.source_label,
            transcription_chars=len(transcription_input.text),
            generated_at=generated_at,
        )
        report_path.write_text(report_body, encoding="utf-8")
        _log(f"  wrote {report_path.relative_to(repo_root)}")

        if result.error:
            _log(f"  [fail] {result.error.splitlines()[0]}")
            failures += 1
        elif result.http_status == 200:
            est_len = len(result.payload.get("estimation", "") or "")
            _log(f"  [ok] HTTP {result.http_status} ({est_len} chars)")
        else:
            detail = result.payload.get("detail", result.payload)
            _log(f"  [fail] HTTP {result.http_status}: {detail}")
            failures += 1

    _log(f"\nDone. Reports in {reports_dir.relative_to(repo_root)}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
