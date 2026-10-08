"""Constants for talking to the Gemini API."""

# Newest free-tier Flash model as of 2026-10. Override with GEMINI_MODEL in .env when a newer one ships.
DEFAULT_GEMINI_MODEL = "gemini-3.8-flash"
JSON_MIME_TYPE = "application/json"

# Error detail returned with HTTP 503 when no Gemini API key is configured on the server
GEMINI_API_KEY_MISSING_DETAIL = "GEMINI_API_KEY is not set on the server."
