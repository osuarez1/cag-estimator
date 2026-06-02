"""Google Gemini adapter (google-genai)."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from typing import Any

import anyio

from app.config import settings
from app.services.llm.errors import map_gemini_exception
from app.services.llm.pricing import estimate_cost
from app.services.llm.types import LLMError, LLMResult, LLMStreamChunk, LLMUsage


def _client():
    from google import genai

    return genai.Client(api_key=settings.google_api_key)


async def generate(
    prompt: str,
    *,
    system: str | None,
    model: str,
    temperature: float,
    max_output_tokens: int,
) -> LLMResult:
    from google.genai import types

    client = _client()

    try:
        config_params: dict[str, Any] = {
            "temperature": temperature,
            "max_output_tokens": max_output_tokens,
        }
        if system:
            config_params["system_instruction"] = system

        resp = await anyio.to_thread.run_sync(
            lambda: client.models.generate_content(
                model=model,
                contents=prompt,
                config=types.GenerateContentConfig(**config_params),
            )
        )

        finish_reason = resp.candidates[0].finish_reason.name
        if finish_reason == "SAFETY":
            return LLMResult(
                provider="gemini",
                model=str(getattr(resp, "model_version", model)),
                error=LLMError(
                    code="safety",
                    message="Response blocked by safety filters",
                    provider="gemini",
                    raw_code=finish_reason,
                ),
            )

        usage_raw = getattr(resp, "usage_metadata", None)
        usage = None
        if usage_raw is not None:
            usage = LLMUsage(
                input_tokens=int(getattr(usage_raw, "prompt_token_count", 0) or 0),
                output_tokens=int(getattr(usage_raw, "candidates_token_count", 0) or 0),
                thinking_tokens=int(getattr(usage_raw, "thoughts_token_count", 0) or 0),
            )

        cost = estimate_cost("gemini", model, usage or LLMUsage())

        return LLMResult(
            provider="gemini",
            model=str(getattr(resp, "model_version", model)),
            content=str(getattr(resp, "text", "") or ""),
            usage=usage,
            finish_reason=str(finish_reason),
            cost_usd=cost,
        )

    except Exception as e:  # noqa: BLE001 - normalize SDK errors
        return LLMResult(provider="gemini", model=model, error=map_gemini_exception(e))


async def stream(
    prompt: str,
    *,
    system: str | None,
    model: str,
    temperature: float,
    max_output_tokens: int,
) -> AsyncIterator[LLMStreamChunk]:
    """
    Gemini streaming uses a sync iterator; we bridge it to async.
    """

    from google.genai import types

    client = _client()

    config_params: dict[str, Any] = {
        "temperature": temperature,
        "max_output_tokens": max_output_tokens,
    }
    if system:
        config_params["system_instruction"] = system

    def _iter() -> Iterator[Any]:
        return client.models.generate_content_stream(
            model=model,
            contents=prompt,
            config=types.GenerateContentConfig(**config_params),
        )

    send, recv = anyio.create_memory_object_stream[LLMStreamChunk](max_buffer_size=100)

    async def _producer() -> None:
        try:
            def _run_sync() -> list[Any]:
                return list(_iter())

            # Collect sync stream responses without blocking event loop.
            responses = await anyio.to_thread.run_sync(_run_sync)

            last = None
            for r in responses:
                last = r
                delta = getattr(r, "text", None)
                if delta:
                    await send.send(LLMStreamChunk(delta=str(delta), provider="gemini", model=model))

            if last is not None:
                finish_reason = last.candidates[0].finish_reason.name
                usage_raw = getattr(last, "usage_metadata", None)
                usage = None
                if usage_raw is not None:
                    usage = LLMUsage(
                        input_tokens=int(getattr(usage_raw, "prompt_token_count", 0) or 0),
                        output_tokens=int(getattr(usage_raw, "candidates_token_count", 0) or 0),
                        thinking_tokens=int(getattr(usage_raw, "thoughts_token_count", 0) or 0),
                    )
                cost = estimate_cost("gemini", model, usage or LLMUsage())
                await send.send(
                    LLMStreamChunk(
                        done=True,
                        provider="gemini",
                        model=str(getattr(last, "model_version", model)),
                        usage=usage,
                        finish_reason=str(finish_reason),
                        cost_usd=cost,
                    )
                )
            else:
                await send.send(LLMStreamChunk(done=True, provider="gemini", model=model))

        except Exception as e:  # noqa: BLE001
            await send.send(LLMStreamChunk(done=True, error=map_gemini_exception(e)))
        finally:
            await send.aclose()

    async with anyio.create_task_group() as tg:
        tg.start_soon(_producer)
        async with recv:
            async for chunk in recv:
                yield chunk

