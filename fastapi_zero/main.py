# fastapi_zero/main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from fastapi_zero.core.config import settings
from fastapi_zero.routers import api, pages

app = FastAPI(title=settings.APP_TITLE)

# Montar arquivos estáticos
app.mount('/static', StaticFiles(directory='static'), name='static')

# Incluir routers
app.include_router(pages.router)
app.include_router(api.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("fastapi_zero.main:app", host="0.0.0.0", port=8000, reload=True)
