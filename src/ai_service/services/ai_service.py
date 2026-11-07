import logging


class AIService:
    """
    Application/service layer.

    This component contains the application's AI-related business logic.
    In Week 03 we implemented classification concepts. Here we expose
    that capability as a service that can later be replaced by an ML
    model or an LLM.
    """

    def __init__(self, logger: logging.Logger) -> None:
        self.logger = logger

    def classify(self, text: str) -> dict[str, str]:
        """
        Classify a piece of text using a simple rule-based implementation.

        This is intentionally simple. The Week 04 goal is architecture,
        not sophisticated machine learning.
        """

        if not isinstance(text, str):
            raise TypeError("text must be a string")

        text = text.strip()

        if not text:
            raise ValueError("Text cannot be empty.")

        normalized_text = text.lower()

        self.logger.info("Classifying text")

        if "password" in normalized_text:
            category = "account"

        elif "fee" in normalized_text or "payment" in normalized_text:
            category = "finance"

        elif (
            "server" in normalized_text
            or "api" in normalized_text
            or "error" in normalized_text
        ):
            category = "technical"

        elif "admission" in normalized_text:
            category = "admission"

        elif "lab" in normalized_text or "classroom" in normalized_text:
            category = "facilities"
        else:
            category = "other"

        self.logger.info("Classification completed: %s", category)

        return {
            "text": text,
            "category": category,
        }