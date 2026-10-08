"""Schemas for the Gemini router."""

from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    """A prompt to send to Gemini."""

    prompt: str = Field(min_length=1)
    system_instruction: str | None = None


class GenerateResponse(BaseModel):
    """Gemini's reply and the model that produced it."""

    text: str
    model: str
