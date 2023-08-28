from fastapi import APIRouter

routes = APIRouter()


@routes.get("/all/")
async def read_characters_all():
    return [
        {"character_id": "1", "character_name": "Aragorn"},
        {"character_id": "2", "character_name": "Ghazh Ironhide"},
    ]
