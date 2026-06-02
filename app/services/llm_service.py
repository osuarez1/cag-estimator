"""LLM provider dispatch (OpenAI, Anthropic, Gemini).

This is the public service facade. Provider SDK integration lives under `app/services/llm/`.
"""

from __future__ import annotations

from collections.abc import AsyncIterator
from textwrap import dedent
from typing import Literal

from app.config import settings
from app.context.examples import EXAMPLES
from app.services.llm.types import LLMResult, LLMStreamChunk

LLMProvider = Literal["openai", "anthropic", "gemini"]

_DEFAULT_MODELS: dict[LLMProvider, str] = {
    "openai": "gpt-4o-mini",
    "anthropic": "claude-3-5-haiku-latest",
    "gemini": "gemini-2.0-flash",
}


def _resolve_model(provider: LLMProvider) -> str:
    if "llm_model" in settings.model_fields_set:
        return settings.llm_model
    return _DEFAULT_MODELS[provider]


async def complete(
    prompt: str,
    *,
    system_prompt: str | None = None,
    model: str | None = None,
    temperature: float = 0.3,
    max_output_tokens: int = 1000,
) -> LLMResult:
    provider = settings.llm_provider
    resolved_model = model or _resolve_model(provider)
    if not settings.active_provider_api_key():
        from app.services.llm.types import LLMError

        return LLMResult(
            provider=provider,
            model=resolved_model,
            error=LLMError(code="auth", message="Invalid or missing API key", provider=provider),
        )

    if provider == "openai":
        from app.services.llm.openai_provider import generate

        return await generate(
            prompt,
            system=system_prompt,
            model=resolved_model,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        )
    if provider == "anthropic":
        from app.services.llm.anthropic_provider import generate

        return await generate(
            prompt,
            system=system_prompt,
            model=resolved_model,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        )
    if provider == "gemini":
        from app.services.llm.gemini_provider import generate

        return await generate(
            prompt,
            system=system_prompt,
            model=resolved_model,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        )

    raise ValueError(f"Unsupported LLM_PROVIDER: {provider!r}")


async def complete_text(
    prompt: str,
    *,
    system_prompt: str | None = None,
    model: str | None = None,
    temperature: float = 0.3,
    max_output_tokens: int = 1000,
) -> str:
    result = await complete(
        prompt,
        system_prompt=system_prompt,
        model=model,
        temperature=temperature,
        max_output_tokens=max_output_tokens,
    )
    return result.content


async def stream_complete(
    prompt: str,
    *,
    system_prompt: str | None = None,
    model: str | None = None,
    temperature: float = 0.3,
    max_output_tokens: int = 1000,
) -> AsyncIterator[LLMStreamChunk]:
    provider = settings.llm_provider
    resolved_model = model or _resolve_model(provider)
    if not settings.active_provider_api_key():
        from app.services.llm.types import LLMError

        yield LLMStreamChunk(
            done=True,
            error=LLMError(code="auth", message="Invalid or missing API key", provider=provider),
        )
        return

    if provider == "openai":
        from app.services.llm.openai_provider import stream

        async for chunk in stream(
            prompt,
            system=system_prompt,
            model=resolved_model,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        ):
            yield chunk
        return
    if provider == "anthropic":
        from app.services.llm.anthropic_provider import stream

        async for chunk in stream(
            prompt,
            system=system_prompt,
            model=resolved_model,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        ):
            yield chunk
        return
    if provider == "gemini":
        from app.services.llm.gemini_provider import stream

        async for chunk in stream(
            prompt,
            system=system_prompt,
            model=resolved_model,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        ):
            yield chunk
        return

    raise ValueError(f"Unsupported LLM_PROVIDER: {provider!r}")


async def estimate(user_input: str) -> dict:
    examples_lines: list[str] = []
    for i, ex in enumerate(EXAMPLES, start=1):
        meeting_summary = (ex.get("meeting_summary") or "").strip()
        estimation = dedent(ex.get("estimation") or "").strip()
        examples_lines.extend(
            [
                f"### Example {i}",
                "",
                "Meeting summary:",
                meeting_summary,
                "",
                "Estimation (markdown):",
                estimation,
                "",
                "---",
                "",
            ]
        )
    examples_block = "\n".join(examples_lines).strip()

    system_prompt = dedent(
        f"""
        You are an expert software estimator.

        Your job is to read a meeting transcript and produce a detailed software estimation in markdown,
        grounded in the transcript and calibrated using the provided historical examples.

        Output requirements:
        - Return markdown only.
        - Start with a clear title like: "## Estimation: <project name>"
        - Include a "### Task Breakdown" section with numbered items and hours per task.
        - Include totals and any relevant assumptions/risks.
        - Include "Recommended team" and "Estimated duration" if reasonably inferable.
        - Be specific and realistic; do not invent requirements not supported by the transcript.

        ## Reference examples (historical)
        {examples_block}
        """
    ).strip()

    provider: LLMProvider = settings.llm_provider
    if provider == "openai":
        resolved_model = "gpt-4o-mini"
    elif provider == "anthropic":
        resolved_model = "claude-haiku-4-5"
    else:
        resolved_model = None

    result_text = await complete_text(
        user_input,
        system_prompt=system_prompt,
        model=resolved_model,
        temperature=0.3,
        max_output_tokens=1200,
    )
    return {"estimation": result_text}
