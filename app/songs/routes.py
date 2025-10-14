from typing import List
from fastapi import APIRouter

from app.songs.schemas import Song, SongCreate

router = APIRouter()

# Retorna a lista de músicas
# [Song] está sendo usado como estrutura, e importado do schemas
@router.get("/", response_model=List[Song]) 
def get_songs():
   return [
        { "title": "Song A", "artist": "Artist A","genre": "Heavy Metal", "duration": 3.5, "id": 1},
        { "title": "Song B", "artist": "Artist B","genre": "Rock", "duration": 4.0, "id": 2}
    ]

@router.post("/", response_model=Song)
def create_song(song: SongCreate):
    new_song = {
        "id": 3,                  # normalmente você gera no DB
        **song.model_dump() # ele transforma o objeto pydantic em dict do python normal, pega esses dados e distribui de acordo
    }
    return new_song
   