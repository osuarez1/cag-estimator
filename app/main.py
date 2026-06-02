"""FastAPI application entrypoint."""

import logging

from fastapi import FastAPI

from app.config import settings
from app.routers import estimations

logging.basicConfig(level=getattr(logging, settings.log_level))
logger = logging.getLogger(__name__)
logger.info("Starting cag-estimator (APP_ENV=%s)", settings.app_env)

app = FastAPI(
    title="Software Estimation API",
    description="API for generating project estimates using LLMs",
)
app.include_router(estimations.router, prefix="/api/v1")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "estimation-api"}
