"""OpenAI adapter (Responses API)."""

from __future__ import annotations

from collections.abc import AsyncIterator

from app.config import settings
from app.services.llm.errors import map_openai_exception
from app.services.llm.pricing import estimate_cost
from app.services.llm.types import LLMError, LLMResult, LLMStreamChunk, LLMUsage


async def generate(
    prompt: str,
    *,
    system: str | None,
    model: str,
    temperature: float,
    max_output_tokens: int,
) -> LLMResult:
    from openai import AsyncOpenAI

    client = AsyncOpenAI(api_key=settings.openai_api_key)

    try:
        resp = await client.responses.create(
            model=model,
            input=prompt,
            instructions=system,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
            store=False,
        )

        # Verify the response is complete
        status = getattr(resp, "status", None)
        if status and status != "completed":
            err = LLMError(code="incomplete", message=f"Response not completed: {status}", provider="openai")
            return LLMResult(provider="openai", model=model, request_id=getattr(resp, "id", None), error=err)

        usage_raw = getattr(resp, "usage", None)
        usage = None
        if usage_raw is not None:
            usage = LLMUsage(
                input_tokens=int(getattr(usage_raw, "input_tokens", 0) or 0),
                output_tokens=int(getattr(usage_raw, "output_tokens", 0) or 0),
            )

        cost = estimate_cost("openai", model, usage or LLMUsage())

        return LLMResult(
            provider="openai",
            model=str(getattr(resp, "model", model)),
            request_id=getattr(resp, "id", None),
            content=str(getattr(resp, "output_text", "") or ""),
            usage=usage,
            finish_reason=str(status) if status else None,
            cost_usd=cost,
        )
    except Exception as e:  # noqa: BLE001 - normalize SDK errors
        return LLMResult(provider="openai", model=model, error=map_openai_exception(e))


async def stream(
    prompt: str,
    *,
    system: str | None,
    model: str,
    temperature: float,
    max_output_tokens: int,
) -> AsyncIterator[LLMStreamChunk]:
    """
    Stream text deltas. Final chunk includes usage/cost when available.
    """

    from openai import AsyncOpenAI

    client = AsyncOpenAI(api_key=settings.openai_api_key)

    try:
        async with client.responses.stream(
            model=model,
            input=prompt,
            instructions=system,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
            store=False,
        ) as stream:
            async for event in stream:
                event_type = getattr(event, "type", "")
                # Matches openai Responses streaming event types:
                # - response.output_text.delta
                if event_type == "response.output_text.delta":
                    delta = getattr(event, "delta", "") or ""
                    if delta:
                        yield LLMStreamChunk(delta=str(delta), provider="openai", model=model)

            final = await stream.get_final_response()

        usage_raw = getattr(final, "usage", None)
        usage = None
        if usage_raw is not None:
            usage = LLMUsage(
                input_tokens=int(getattr(usage_raw, "input_tokens", 0) or 0),
                output_tokens=int(getattr(usage_raw, "output_tokens", 0) or 0),
            )
        cost = estimate_cost("openai", model, usage or LLMUsage())

        yield LLMStreamChunk(
            done=True,
            provider="openai",
            model=str(getattr(final, "model", model)),
            usage=usage,
            finish_reason=str(getattr(final, "status", None) or ""),
            cost_usd=cost,
        )

    except Exception as e:  # noqa: BLE001 - normalize SDK errors
        yield LLMStreamChunk(done=True, error=map_openai_exception(e))

