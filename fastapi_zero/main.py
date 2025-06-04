# fastapi_zero/main.py
from contextlib import asynccontextmanager
from logging import getLogger

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from fastapi_zero.core.config import settings
from fastapi_zero.routers import api, pages

logger = getLogger('uvicorn')


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info('Iniciando a aplicação')
    yield  # Executa a aplicação
    logger.info('Finalizando a aplicação')


app = FastAPI(title=settings.APP_TITLE, lifespan=lifespan)

# Montar arquivos estáticos
app.mount('/static', StaticFiles(directory='static'), name='static')

# Incluir routers
app.include_router(pages.router)
app.include_router(api.router, prefix='/api')

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('fastapi_zero.main:app', host='0.0.0.0', port=8000, reload=True)
