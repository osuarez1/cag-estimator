"""Estimations HTTP endpoints."""

from fastapi import APIRouter
from pydantic import BaseModel

from app.services import llm_service

router = APIRouter(prefix="/estimations", tags=["estimations"])


class EstimationRequest(BaseModel):
    input: str


@router.post("")
async def create_estimation(req: EstimationRequest) -> dict:
    return await llm_service.estimate(req.input)

