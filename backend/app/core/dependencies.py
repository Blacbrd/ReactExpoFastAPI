"""FastAPI dependencies shared across routers."""

from functools import lru_cache

from fastapi import HTTPException, status

from app.core.config import get_settings
from app.utils.gemini_client import GeminiClient
from app.utils.gemini_constants import GEMINI_API_KEY_MISSING_DETAIL


@lru_cache
def get_gemini_client() -> GeminiClient:
    """Return a shared Gemini client, or fail with 503 when no API key is configured."""
    settings = get_settings()
    api_key = settings.gemini_api_key.get_secret_value() if settings.gemini_api_key else ""
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=GEMINI_API_KEY_MISSING_DETAIL,
        )
    return GeminiClient(api_key=api_key, model=settings.gemini_model)


async def close_gemini_client() -> None:
    """Close the shared Gemini client if one was ever created."""
    if get_gemini_client.cache_info().currsize:
        await get_gemini_client().close()
        get_gemini_client.cache_clear()
