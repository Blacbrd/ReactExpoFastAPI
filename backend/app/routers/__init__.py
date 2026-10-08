"""Aggregates every feature router into a single `api_router`."""

from fastapi import APIRouter

from app.routers import gemini, health, items

api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(items.router)
api_router.include_router(gemini.router)
