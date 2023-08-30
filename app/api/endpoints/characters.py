from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from app.db.models import characters
from settings import SessionLocal

routes = APIRouter()
session = SessionLocal()


@routes.get("/all/")
async def read_characters_all():
    characters_data = session.query(characters.Character).all()
    return jsonable_encoder(characters_data)
