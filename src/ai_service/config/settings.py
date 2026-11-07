import os

from dotenv import load_dotenv

# Load variables from .env when running locally.
load_dotenv()


class Settings:
    """
    Central application configuration.

    Configuration should come from the environment rather than
    being hard-coded inside application logic.
    """

    APP_NAME: str = os.getenv("APP_NAME", "Week 04 AI Service")
    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))


settings = Settings()