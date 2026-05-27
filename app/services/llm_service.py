"""LLM provider dispatch (OpenAI, Anthropic, Gemini)."""

from __future__ import annotations

from typing import Literal

from app.config import settings
from app.context.examples import EXAMPLES

LLMProvider = Literal["openai", "anthropic", "gemini"]


def _resolve_model(provider: LLMProvider) -> str:
    if settings.llm_model:
        return settings.llm_model
    if provider == "openai":
        return "gpt-4o-mini"
    if provider == "anthropic":
        return "claude-3-5-haiku-latest"
    return "gemini-2.0-flash"


def _call_openai(prompt: str, model: str) -> str:
    if not settings.openai_api_key:
        raise ValueError("OPENAI_API_KEY is required when LLM_PROVIDER=openai.")

    from openai import OpenAI

    client = OpenAI(api_key=settings.openai_api_key)
    resp = client.responses.create(
        model=model,
        input=prompt,
    )
    return resp.output_text


def _call_anthropic(prompt: str, model: str) -> str:
    if not settings.anthropic_api_key:
        raise ValueError("ANTHROPIC_API_KEY is required when LLM_PROVIDER=anthropic.")

    import anthropic

    client = anthropic.Anthropic(api_key=settings.anthropic_api_key)
    msg = client.messages.create(
        model=model,
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}],
    )
    return "".join(block.text for block in msg.content if hasattr(block, "text"))


def _call_gemini(prompt: str, model: str) -> str:
    if not settings.google_api_key:
        raise ValueError("GOOGLE_API_KEY is required when LLM_PROVIDER=gemini.")

    from google import genai

    client = genai.Client(api_key=settings.google_api_key)
    resp = client.models.generate_content(model=model, contents=prompt)
    return resp.text or ""


def complete(prompt: str) -> str:
    provider = settings.llm_provider
    model = _resolve_model(provider)

    if provider == "openai":
        return _call_openai(prompt, model)
    if provider == "anthropic":
        return _call_anthropic(prompt, model)
    if provider == "gemini":
        return _call_gemini(prompt, model)

    raise ValueError(f"Unsupported LLM_PROVIDER: {provider!r}")


async def estimate(user_input: str) -> dict:
    # Scaffold: do not call real LLM by default.
    # EXAMPLES is wired in so CAG prompt assembly can be added next.
    _ = EXAMPLES
    return {"status": "not_implemented", "input": user_input}

