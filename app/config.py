"""Application settings loaded from environment."""

from __future__ import annotations

from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    llm_provider: Literal["openai", "anthropic", "gemini"] = "openai"
    llm_model: str | None = None

    openai_api_key: str | None = None
    anthropic_api_key: str | None = None
    google_api_key: str | None = None


settings = Settings()

