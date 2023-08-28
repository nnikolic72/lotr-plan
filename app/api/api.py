from fastapi import APIRouter
from app.api.endpoints.characters import routes as characters_router

router = APIRouter()

router.include_router(characters_router, prefix="/characters", tags=["characters"])
