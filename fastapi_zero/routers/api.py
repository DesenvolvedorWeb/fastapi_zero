# fastapi_zero/routers/api.py
from datetime import datetime
from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends

from fastapi_zero.core.security import get_current_user
from fastapi_zero.schemas.schemas import APIResponse, Message

router = APIRouter()


@router.get('/hello', response_model=Message)
async def hello():
    """Endpoint público que retorna uma mensagem de saudação."""
    return Message(
        message='Hello World', status=HTTPStatus.OK, timestamp=datetime.now()
    )


@router.get('/stats', status_code=HTTPStatus.OK)
async def api_stats(username: Annotated[str, Depends(get_current_user)]):
    """
    Retorna estatísticas do sistema em formato JSON.
    Requer autenticação básica.
    """
    return APIResponse(
        success=True, data={'users': 1250, 'active': 847, 'requests': 12345}
    )


@router.get('/me', status_code=HTTPStatus.OK)
async def current_user(username: Annotated[str, Depends(get_current_user)]):
    """Retorna informações sobre o usuário autenticado."""
    return APIResponse(
        success=True,
        data={'username': username, 'role': 'admin', 'authenticated': True},
    )


# Adicione outras rotas de API conforme necessário
