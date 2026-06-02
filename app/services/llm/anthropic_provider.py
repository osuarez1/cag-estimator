"""Anthropic adapter (Messages API)."""

from __future__ import annotations

from collections.abc import AsyncIterator

from app.config import settings
from app.services.llm.errors import map_anthropic_exception
from app.services.llm.pricing import estimate_cost
from app.services.llm.types import LLMResult, LLMStreamChunk, LLMUsage


async def generate(
    prompt: str,
    *,
    system: str | None,
    model: str,
    temperature: float,
    max_output_tokens: int,
) -> LLMResult:
    from anthropic import AsyncAnthropic

    client = AsyncAnthropic(api_key=settings.anthropic_api_key)

    try:
        kwargs = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_output_tokens,
            "temperature": temperature,
        }
        if system:
            kwargs["system"] = system

        msg = await client.messages.create(**kwargs)

        usage_raw = getattr(msg, "usage", None)
        usage = None
        if usage_raw is not None:
            usage = LLMUsage(
                input_tokens=int(getattr(usage_raw, "input_tokens", 0) or 0),
                output_tokens=int(getattr(usage_raw, "output_tokens", 0) or 0),
            )

        cost = estimate_cost("anthropic", model, usage or LLMUsage())
        content = "".join(block.text for block in msg.content if hasattr(block, "text"))

        return LLMResult(
            provider="anthropic",
            model=str(getattr(msg, "model", model)),
            request_id=getattr(msg, "id", None),
            content=content,
            usage=usage,
            finish_reason=str(getattr(msg, "stop_reason", None) or ""),
            cost_usd=cost,
        )
    except Exception as e:  # noqa: BLE001 - normalize SDK errors
        return LLMResult(provider="anthropic", model=model, error=map_anthropic_exception(e))


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

    Note: Anthropic streaming yields multiple event types; we only surface text deltas.
    """

    from anthropic import AsyncAnthropic

    client = AsyncAnthropic(api_key=settings.anthropic_api_key)

    try:
        kwargs = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_output_tokens,
            "temperature": temperature,
        }
        if system:
            kwargs["system"] = system

        async with client.messages.stream(**kwargs) as stream:
            async for event in stream:
                # event objects have a `type` field; deltas often carry `.delta.text`
                event_type = getattr(event, "type", "")
                if event_type == "content_block_delta":
                    delta = getattr(getattr(event, "delta", None), "text", None)
                    if delta:
                        yield LLMStreamChunk(delta=str(delta), provider="anthropic", model=model)

            final_msg = await stream.get_final_message()

        usage_raw = getattr(final_msg, "usage", None)
        usage = None
        if usage_raw is not None:
            usage = LLMUsage(
                input_tokens=int(getattr(usage_raw, "input_tokens", 0) or 0),
                output_tokens=int(getattr(usage_raw, "output_tokens", 0) or 0),
            )
        cost = estimate_cost("anthropic", model, usage or LLMUsage())

        yield LLMStreamChunk(
            done=True,
            provider="anthropic",
            model=str(getattr(final_msg, "model", model)),
            usage=usage,
            finish_reason=str(getattr(final_msg, "stop_reason", None) or ""),
            cost_usd=cost,
        )
    except Exception as e:  # noqa: BLE001 - normalize SDK errors
        yield LLMStreamChunk(done=True, error=map_anthropic_exception(e))

