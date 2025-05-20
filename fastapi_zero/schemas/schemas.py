# fastapi_zero/schemas/schemas.py
from datetime import datetime
from http import HTTPStatus
from typing import Dict, Optional

from pydantic import BaseModel, Field


class Message(BaseModel):
    message: str
    status: HTTPStatus
    timestamp: datetime
    details: Optional[str] = None


class DashboardStats(BaseModel):
    users: int = Field(..., description='Número total de usuários')
    active: int = Field(..., description='Usuários ativos')
    requests: int = Field(..., description='Total de requisições')


class DashboardData(BaseModel):
    message: str
    description: str
    stats: DashboardStats
    version: str
    environment: str
    current_date: str


class APIResponse(BaseModel):
    success: bool
    data: Optional[Dict] = None
    error: Optional[str] = None
