from pydantic import BaseModel

# Para criar ou atualizar uma música
class SongCreate(BaseModel):
    title: str
    artist: str
    genre: str
    duration: float


# Para retornar dados da música, incluindo o id - herda o SongCreate
class Song(SongCreate):
    id: int



class Config:
    orm_mode = True  # necessário para trabalhar com SQLAlchemy