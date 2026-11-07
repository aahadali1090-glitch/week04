import pytest
from fastapi.testclient import TestClient

from ai_service.main import app
from ai_service.services.ai_service import AIService


client = TestClient(app)


def test_password_classification() -> None:
    response = client.post(
        "/classify",
        params={"text": "I forgot my password"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["category"] == "account"


def test_fee_classification() -> None:
    response = client.post(
        "/classify",
        params={"text": "I have a problem with my fee"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["category"] == "finance"


def test_technical_classification() -> None:
    response = client.post(
        "/classify",
        params={"text": "The server is down"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["category"] == "technical"


def test_unknown_classification() -> None:
    response = client.post(
        "/classify",
        params={"text": "I need some information"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["category"] == "other"


def test_empty_text() -> None:
    response = client.post(
        "/classify",
        params={"text": ""},
    )

    assert response.status_code == 400


def test_service_directly() -> None:
    """
    Test the service component without HTTP.
    """

    logger = __import__("logging").getLogger("test")

    service = AIService(logger)

    result = service.classify("I forgot my password")

    assert result["category"] == "account"

def test_version_endpoint():
    from ai_service.config.settings import settings
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": settings.APP_VERSION}

def test_facilities_classification():
    response = client.post("/classify", params={"text": "The classroom is closed"})
    assert response.status_code == 200
    assert response.json()["category"] == "facilities"
