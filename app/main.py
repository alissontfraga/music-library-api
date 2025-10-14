import uvicorn
from fastapi import FastAPI

from app.songs.routes import router as songs_router  #pega o router que defini em routes.py

app = FastAPI()


# Adiciona todas as rotas do router ao FastAPI, com prefixo /songs na URL.
app.include_router(songs_router, prefix="/songs")







# Pra rodar o sistema
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
