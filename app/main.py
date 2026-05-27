"""FastAPI application entrypoint."""

from fastapi import FastAPI

from app.routers import estimations

app = FastAPI(title="estimador-cag")
app.include_router(estimations.router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}

