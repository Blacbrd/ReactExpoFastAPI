"""Router that forwards prompts to Gemini."""

from typing import Annotated

from fastapi import APIRouter, Depends

from app.core.dependencies import get_gemini_client
from app.schemas.gemini import GenerateRequest, GenerateResponse
from app.utils.gemini_client import GeminiClient

router = APIRouter(prefix="/gemini", tags=["gemini"])

GeminiDep = Annotated[GeminiClient, Depends(get_gemini_client)]


@router.post("/generate")
async def generate(payload: GenerateRequest, gemini: GeminiDep) -> GenerateResponse:
    """Send a prompt to Gemini and return its text reply."""
    text = await gemini.generate_text(payload.prompt, payload.system_instruction)
    return GenerateResponse(text=text, model=gemini.model)
