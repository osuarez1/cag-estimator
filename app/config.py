"""Application settings loaded from environment.

Note: API keys are not validated at import time so the app can start (e.g. `/health`)
without secrets present. Provider-specific calls validate keys at runtime.
"""

from __future__ import annotations

import os
from typing import Literal, Self

from pydantic_settings import BaseSettings, SettingsConfigDict

LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
LLMProvider = Literal["openai", "anthropic", "gemini", "mock"]

_PROVIDER_KEY: dict[LLMProvider, tuple[str, str | None]] = {
    "openai": ("OPENAI_API_KEY", "openai_api_key"),
    "anthropic": ("ANTHROPIC_API_KEY", "anthropic_api_key"),
    "gemini": ("GOOGLE_API_KEY", "google_api_key"),
    "mock": ("", None),
}


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    openai_api_key: str | None = None
    anthropic_api_key: str | None = None
    google_api_key: str | None = None

    llm_provider: LLMProvider = "openai"
    llm_model: str = "gpt-4o-mini"

    app_env: str = "development"
    log_level: LogLevel = "DEBUG"

    def active_provider_api_key(self) -> str | None:
        _, attr = _PROVIDER_KEY[self.llm_provider]
        if not attr:
            return None
        val = getattr(self, attr)
        return val or None


settings = Settings()

def _coalesce_env(*names: str) -> str | None:
    for n in names:
        v = os.getenv(n)
        if v:
            return v
    return None


# Runtime evidence (infisical) shows injected names are OPENAI_SECRET / ANTHROPIC_SECRET / GOOGLE_SECRET.
# We coalesce to the expected Settings fields without logging values.
if not settings.openai_api_key:
    settings.openai_api_key = _coalesce_env("OPENAI_SECRET")
if not settings.anthropic_api_key:
    settings.anthropic_api_key = _coalesce_env("ANTHROPIC_SECRET")
if not settings.google_api_key:
    settings.google_api_key = _coalesce_env("GOOGLE_SECRET")
