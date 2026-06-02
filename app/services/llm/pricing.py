"""Per-model pricing (USD per 1M tokens). Update periodically from provider docs."""

from __future__ import annotations

from app.services.llm.types import LLMProvider, LLMUsage

# provider -> model -> {input, output, thinking?} in USD per 1M tokens
PRICING: dict[LLMProvider, dict[str, dict[str, float]]] = {
    "openai": {
        "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    },
    "anthropic": {
        "claude-haiku-4-5-20251001": {"input": 1.00, "output": 5.00},
        "claude-3-5-haiku-latest": {"input": 1.00, "output": 5.00},
    },
    "gemini": {
        "gemini-2.5-flash": {"input": 0.15, "output": 0.60, "thinking": 3.50},
        "gemini-2.0-flash": {"input": 0.10, "output": 0.40, "thinking": 0.0},
    },
}

_DEFAULT_RATES: dict[str, float] = {
    "input": 0.0,
    "output": 0.0,
    "thinking": 0.0,
}


def estimate_cost(provider: LLMProvider, model: str, usage: LLMUsage) -> float:
    rates = PRICING.get(provider, {}).get(model, _DEFAULT_RATES)
    return (
        (usage.input_tokens / 1_000_000) * rates.get("input", 0.0)
        + (usage.output_tokens / 1_000_000) * rates.get("output", 0.0)
        + (usage.thinking_tokens / 1_000_000) * rates.get("thinking", 0.0)
    )
