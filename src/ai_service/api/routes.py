from fastapi import APIRouter, HTTPException
from ai_service.config.settings import settings

from ai_service.services.ai_service import AIService
from ai_service.utils.logging import configure_logging


router = APIRouter()

logger = configure_logging()
ai_service = AIService(logger)


@router.get("/")
def root() -> dict[str, str]:
    """
    Basic service information.
    """

    return {
        "message": "AI Service is running",
        "version": settings.APP_VERSION,
    }


@router.get("/health")
def health() -> dict[str, str]:
    """
    Health check endpoint.

    Used by operators, load balancers and deployment systems
    to determine whether the service is responding.
    """

    return {
        "status": "healthy",
    }


@router.post("/classify")
def classify(text: str) -> dict[str, str]:
    """
    Classify input text.
    """

    try:
        return ai_service.classify(text)

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc

    except TypeError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc

@router.get("/version")
def version() -> dict[str, str]:
    return {"version": settings.APP_VERSION}
