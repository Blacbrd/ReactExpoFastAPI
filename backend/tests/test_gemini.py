"""Tests for the Gemini router, with the SDK stubbed out."""

from fastapi.testclient import TestClient

from app.core.dependencies import get_gemini_client
from app.main import app


class FakeGeminiClient:
    """Stands in for GeminiClient so tests never hit the network."""

    model = "fake-model"

    async def generate_text(self, prompt: str, system_instruction: str | None = None) -> str:
        """Echo the prompt back."""
        return f"echo: {prompt}"


def test_generate_returns_model_text(client: TestClient) -> None:
    """The router returns whatever the client generates."""
    app.dependency_overrides[get_gemini_client] = FakeGeminiClient
    response = client.post("/api/gemini/generate", json={"prompt": "hi"})
    assert response.status_code == 200
    assert response.json() == {"text": "echo: hi", "model": "fake-model"}


def test_generate_rejects_empty_prompt(client: TestClient) -> None:
    """Validation rejects an empty prompt before Gemini is called."""
    app.dependency_overrides[get_gemini_client] = FakeGeminiClient
    assert client.post("/api/gemini/generate", json={"prompt": ""}).status_code == 422
