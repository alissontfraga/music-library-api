from .songs import router as songs_router

__all__ = ["songs_router"]

# 🔸 Se o __init__.py estiver vazio
# Você teria que escrever no main.py:

# from app.api.routers.songs import router as songs_router

#Isso funciona perfeitamente.
# Ou seja, se você preferir não reexportar nada, pode sim deixar ele vazio e fazer assim.

# 🔸 Se o __init__.py tiver:
#from .songs import router as songs_router
#_ _all__ = ["songs_router"]


#Aí você pode importar de forma mais simples no main.py:

# from app.api.routers import songs_router