"""Map provider SDK exceptions to normalized LLMError values."""

from __future__ import annotations

from typing import Any

from app.services.llm.types import LLMError, LLMErrorCode, LLMProvider


def _err(
    code: LLMErrorCode,
    message: str,
    provider: LLMProvider,
    raw_code: str | int | None = None,
) -> LLMError:
    return LLMError(
        code=code,
        message=message,
        provider=provider,
        raw_code=raw_code,
    )


def map_openai_exception(exc: BaseException, provider: LLMProvider = "openai") -> LLMError:
    from openai import (
        APIConnectionError,
        AuthenticationError,
        BadRequestError,
        InternalServerError,
        RateLimitError,
    )

    if isinstance(exc, AuthenticationError):
        return _err("auth", "Invalid or missing API key", provider)
    if isinstance(exc, RateLimitError):
        return _err("rate_limit", "Rate limit reached or insufficient credit", provider)
    if isinstance(exc, BadRequestError):
        msg = getattr(exc, "message", None) or str(exc)
        return _err("bad_request", f"Invalid request: {msg}", provider)
    if isinstance(exc, (APIConnectionError, InternalServerError)):
        return _err("connection", "Connection or server error", provider)
    return _err("unknown", str(exc), provider)


def map_anthropic_exception(
    exc: BaseException, provider: LLMProvider = "anthropic"
) -> LLMError:
    from anthropic import (
        APIConnectionError,
        AuthenticationError,
        BadRequestError,
        InternalServerError,
        RateLimitError,
    )

    if isinstance(exc, AuthenticationError):
        return _err("auth", "Invalid or missing API key", provider)
    if isinstance(exc, RateLimitError):
        return _err("rate_limit", "Rate limit reached or insufficient credit", provider)
    if isinstance(exc, BadRequestError):
        msg = getattr(exc, "message", None) or str(exc)
        return _err("bad_request", f"Invalid request: {msg}", provider)
    if isinstance(exc, (APIConnectionError, InternalServerError)):
        return _err("connection", "Connection or server error", provider)
    return _err("unknown", str(exc), provider)


def map_gemini_exception(exc: BaseException, provider: LLMProvider = "gemini") -> LLMError:
    from google.genai.errors import APIError, ClientError

    if isinstance(exc, ClientError):
        return _err("bad_request", f"Bad request: {exc}", provider)
    if isinstance(exc, APIError):
        code = getattr(exc, "code", None)
        if code == 429:
            return _err(
                "rate_limit",
                "Rate limit reached or insufficient quota",
                provider,
                raw_code=code,
            )
        message = getattr(exc, "message", None) or str(exc)
        return _err(
            "server",
            f"API error ({code}): {message}",
            provider,
            raw_code=code,
        )
    return _err("unknown", str(exc), provider)


def result_with_error(
    provider: LLMProvider,
    model: str,
    error: LLMError,
) -> Any:
    from app.services.llm.types import LLMResult

    return LLMResult(provider=provider, model=model, error=error)
