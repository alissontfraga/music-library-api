from fastapi import FastAPI
from app.api.routers import songs_router

app = FastAPI()

@app.get("/")
async def root():
   return {"API Music Library": "Funcionando"}
 
app.include_router(songs_router) # prefix="/songs"