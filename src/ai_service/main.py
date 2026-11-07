from contextlib import asynccontextmanager

from fastapi import FastAPI

from ai_service.api.routes import router
from ai_service.config.settings import settings
from ai_service.utils.logging import configure_logging


logger = configure_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup and shutdown lifecycle.

    Code before yield runs during startup.
    Code after yield runs during shutdown.
    """

    logger.info(
        "Starting %s version %s",
        settings.APP_NAME,
        settings.APP_VERSION,
    )

    yield

    logger.info("Shutting down %s", settings.APP_NAME)


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Week 04 Software Architecture and Cloud Foundations",
    lifespan=lifespan,
)

app.include_router(router)