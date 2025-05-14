
# fastapi_zero/routers/api.py
from datetime import datetime
from http import HTTPStatus

from fastapi import APIRouter

from fastapi_zero.schemas.schemas import Message

router = APIRouter()

@router.get("/hello", response_model=Message)
async def hello():
    return Message(
        message="Hello World",
        status=HTTPStatus.OK,
        timestamp=datetime.now()
    )

@router.get("/stats", status_code=HTTPStatus.OK)
async def api_stats():
    """Retorna estatísticas do sistema em formato JSON."""
    return {
        "success": True,
        "data": {
            "users": 1250,
            "active": 847,
            "requests": 12345
        }
    }
# Adicione outras rotas de API conforme necessário

