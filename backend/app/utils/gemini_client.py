"""Thin async wrapper around the Google Gen AI SDK."""

from google import genai
from google.genai import types
from pydantic import BaseModel

from app.utils.gemini_constants import JSON_MIME_TYPE


class GeminiClient:
    """Sends prompts to a single Gemini model and returns plain or structured output."""

    def __init__(self, api_key: str, model: str) -> None:
        """Create the underlying SDK client bound to `model`."""
        self._client = genai.Client(api_key=api_key)
        self.model = model

    async def generate_text(self, prompt: str, system_instruction: str | None = None) -> str:
        """Return the model's text reply to `prompt`."""
        response = await self._client.aio.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(system_instruction=system_instruction),
        )
        return response.text or ""

    async def generate_structured[T: BaseModel](
        self, prompt: str, schema: type[T], system_instruction: str | None = None
    ) -> T:
        """Return the model's reply to `prompt` parsed into `schema`."""
        response = await self._client.aio.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                response_mime_type=JSON_MIME_TYPE,
                response_schema=schema,
            ),
        )
        return schema.model_validate_json(response.text or "")

    async def close(self) -> None:
        """Release the SDK's underlying HTTP connections."""
        await self._client.aio.aclose()
