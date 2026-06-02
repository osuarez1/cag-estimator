"""Estimations HTTP endpoints."""

from __future__ import annotations

from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from app.services import llm_service

router = APIRouter(prefix="/api/v1", tags=["estimations"])


class EstimateRequest(BaseModel):
    transcription: str = Field(min_length=1)


class EstimateResponse(BaseModel):
    estimation: str
    model: str
    provider: str

    input_tokens: int | None = Field(default=None, ge=0)
    output_tokens: int | None = Field(default=None, ge=0)
    thinking_tokens: int | None = Field(default=None, ge=0)
    cost_usd: float | None = Field(default=None, ge=0.0)
    request_id: str | None = None
    finish_reason: str | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


_ERROR_HTTP_STATUS: dict[str, int] = {
    "auth": status.HTTP_401_UNAUTHORIZED,
    "rate_limit": status.HTTP_429_TOO_MANY_REQUESTS,
    "bad_request": status.HTTP_400_BAD_REQUEST,
    "safety": status.HTTP_403_FORBIDDEN,
    "incomplete": status.HTTP_502_BAD_GATEWAY,
    "connection": status.HTTP_502_BAD_GATEWAY,
    "server": status.HTTP_502_BAD_GATEWAY,
    "unknown": status.HTTP_502_BAD_GATEWAY,
}


@router.post("/estimate", response_model=EstimateResponse)
async def estimate(req: EstimateRequest) -> EstimateResponse:
    data = await llm_service.estimate(req.transcription)
    err = data.get("error")
    if err:
        code = err.get("code", "unknown")
        raise HTTPException(
            status_code=_ERROR_HTTP_STATUS.get(code, status.HTTP_502_BAD_GATEWAY),
            detail=err.get("message", "LLM request failed"),
        )
    return EstimateResponse(**data)

