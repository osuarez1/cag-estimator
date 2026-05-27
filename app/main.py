"""FastAPI application entrypoint."""

import logging

from fastapi import FastAPI

from app.config import settings
from app.routers import estimations

logging.basicConfig(level=getattr(logging, settings.log_level))
logger = logging.getLogger(__name__)
logger.info("Starting estimador-cag (APP_ENV=%s)", settings.app_env)

app = FastAPI(title="estimador-cag")
app.include_router(estimations.router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
