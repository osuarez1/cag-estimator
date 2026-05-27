"""Application settings loaded from environment."""

from __future__ import annotations

from typing import Literal, Self

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
LLMProvider = Literal["openai", "anthropic", "gemini"]

_PROVIDER_KEY: dict[LLMProvider, tuple[str, str | None]] = {
    "openai": ("OPENAI_API_KEY", "openai_api_key"),
    "anthropic": ("ANTHROPIC_API_KEY", "anthropic_api_key"),
    "gemini": ("GOOGLE_API_KEY", "google_api_key"),
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

    @model_validator(mode="after")
    def require_active_provider_api_key(self) -> Self:
        env_name, attr = _PROVIDER_KEY[self.llm_provider]
        if not getattr(self, attr):
            raise ValueError(
                f"{env_name} is required when LLM_PROVIDER={self.llm_provider!r}."
            )
        return self


settings = Settings()
