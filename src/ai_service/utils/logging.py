import logging
import sys


def configure_logging() -> logging.Logger:
    """
    Configure application-wide logging.

    Logs are sent to the console so they are visible when the
    application runs locally or inside a Docker container.
    """

    logger = logging.getLogger("ai_service")

    # Avoid adding handlers repeatedly when development reloads.
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger