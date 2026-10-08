# Expo + FastAPI hackathon template

- `frontend/` — Expo / React Native app ([README](frontend/README.md))
- `backend/` — FastAPI + Gemini API ([README](backend/README.md))

## Quick start

```bash
# terminal 1
cd backend && cp .env.example .env && uv sync
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# terminal 2
cd frontend && cp .env.example .env && npm install && npm start
```

On a physical phone, set `EXPO_PUBLIC_API_URL` in `frontend/.env` to your computer's LAN IP, not `localhost`.
