"""Shared LLM request/response types."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

LLMProvider = Literal["openai", "anthropic", "gemini", "mock"]

LLMErrorCode = Literal[
    "auth",
    "rate_limit",
    "bad_request",
    "connection",
    "server",
    "safety",
    "incomplete",
    "unknown",
]


class LLMError(BaseModel):
    model_config = ConfigDict(extra="forbid")

    code: LLMErrorCode
    message: str
    provider: LLMProvider | None = None
    raw_code: str | int | None = None


class LLMUsage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    input_tokens: int = Field(default=0, ge=0)
    output_tokens: int = Field(default=0, ge=0)
    thinking_tokens: int = Field(default=0, ge=0)


class LLMResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    provider: LLMProvider
    model: str
    content: str = ""
    request_id: str | None = None
    usage: LLMUsage | None = None
    finish_reason: str | None = None
    cost_usd: float = Field(default=0.0, ge=0.0)
    error: LLMError | None = None

    @property
    def ok(self) -> bool:
        return self.error is None

    def to_dict(self) -> dict:
        data = self.model_dump(exclude_none=True)
        usage = data.pop("usage", None)
        if usage:
            data["input_tokens"] = usage.get("input_tokens", 0)
            data["output_tokens"] = usage.get("output_tokens", 0)
            thinking = usage.get("thinking_tokens", 0)
            if thinking:
                data["thinking_tokens"] = thinking
        err = data.pop("error", None)
        if err:
            data["error"] = {"code": err["code"], "message": err["message"]}
        return data


class LLMStreamChunk(BaseModel):
    model_config = ConfigDict(extra="forbid")

    delta: str = ""
    provider: LLMProvider | None = None
    model: str | None = None
    usage: LLMUsage | None = None
    finish_reason: str | None = None
    cost_usd: float | None = Field(default=None, ge=0.0)
    error: LLMError | None = None
    done: bool = False
