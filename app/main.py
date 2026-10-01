from fastapi import FastAPI
from pydantic import BaseModel
class HealthCheckResponse(BaseModel):
    status: str


app = FastAPI(
    title="Git Time Machine",
    version="0.1.0",
    )


@app.get("/health", response_model=HealthCheckResponse)
def health_check() -> HealthCheckResponse:
    """
    Health check endpoint to verify that the application is running.
    """
    return HealthCheckResponse(status="ok")
