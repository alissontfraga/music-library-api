from fastapi import APIRouter
from app.api.schemas import Musica

router = APIRouter(prefix="/songs", tags=["Songs"])  # prefix é a / que será usada para esse endpoint, tags é pra aparecer como "Songs" no swagger

# lista que vai armazenar no database
musicas = []

@router.get("/")
def listar_musicas():
    return musicas

@router.get("/nome")
def buscar_musica(nome: str): # anotação de tipo (type hint) do Python, para indicar
    for musica in musicas:
        if musica["nome"].lower() == nome.lower():
            return musica
    return {"erro" : "musica não encontrada"}

@router.post("/")
def adicionar_musica(musica: Musica):#parâmetro chamado musica, objeto do tipo Musica
    musicas.append(musica.model_dump()) # Converte pra dicionário
    return musica

