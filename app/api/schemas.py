from pydantic import BaseModel

class Musica(BaseModel):
    nome: str
    artista: str
    pais: str
    genero: str
    ano: str
    duracao: str # "mm:ss"