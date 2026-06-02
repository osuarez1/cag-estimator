"""Deterministic mock LLM provider for CI and local verification.

This provider never performs network calls and never requires API keys.
"""

from __future__ import annotations

from collections.abc import AsyncIterator

from app.services.llm.types import LLMResult, LLMStreamChunk, LLMUsage


def _estimate_markdown(prompt: str, *, system: str | None, model: str) -> str:
    # Make output stable, but still demonstrably shaped by the injected examples format.
    # We intentionally include markers used in `app/context/examples.py` so verification can assert them.
    project_hint = "Lead routing + enrichment tool"
    if "lead" in prompt.lower():
        project_hint = "Lead routing + enrichment tool"
    elif "e-commerce" in prompt.lower() or "ecommerce" in prompt.lower():
        project_hint = "E-Commerce platform"

    calibrated_hint = ""
    if system and "## Reference examples (historical)" in system:
        calibrated_hint = "Calibrated using historical examples."

    return "\n".join(
        [
            f"## Estimation: {project_hint}",
            "",
            calibrated_hint,
            "",
            "### Task Breakdown",
            "1. Discovery & requirements clarification: 6 hours",
            "2. Data model + persistence (leads, audit trail): 10 hours",
            "3. HubSpot integration (create/update lead): 8 hours",
            "4. Scoring + routing rules + admin config UI/API: 12 hours",
            "5. Rep dashboard + filters + reporting (weekly metrics): 12 hours",
            "6. Slack notifications + event hooks: 4 hours",
            "7. Auth + roles (admin vs rep): 8 hours",
            "8. Testing + QA + deployment checklist: 6 hours",
            "",
            "**Total estimated: 66 hours**",
            "**Recommended team:** 1 Full-stack developer, 1 QA (part-time)",
            "**Estimated duration:** 4-6 weeks (MVP)",
            "",
            "### Assumptions / Risks",
            "- HubSpot API access and field mappings are available.",
            "- Reporting requirements may expand; metrics definitions should be finalized early.",
        ]
    ).strip() + "\n"


async def generate(
    prompt: str,
    *,
    system: str | None = None,
    model: str = "mock-1",
    temperature: float = 0.0,
    max_output_tokens: int = 1200,
) -> LLMResult:
    _ = (temperature, max_output_tokens)
    content = _estimate_markdown(prompt, system=system, model=model)
    usage = LLMUsage(input_tokens=max(len(prompt) // 4, 1), output_tokens=max(len(content) // 4, 1))
    return LLMResult(provider="mock", model=model, content=content, usage=usage, finish_reason="stop")


async def stream(
    prompt: str,
    *,
    system: str | None = None,
    model: str = "mock-1",
    temperature: float = 0.0,
    max_output_tokens: int = 1200,
) -> AsyncIterator[LLMStreamChunk]:
    _ = (temperature, max_output_tokens)
    content = _estimate_markdown(prompt, system=system, model=model)
    # Split deterministically so downstream can validate streaming if needed.
    for piece in content.splitlines(keepends=True):
        yield LLMStreamChunk(delta=piece, provider="mock", model=model)
    yield LLMStreamChunk(done=True, provider="mock", model=model, finish_reason="stop")

