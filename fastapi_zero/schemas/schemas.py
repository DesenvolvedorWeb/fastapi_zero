
# fastapi_zero/schemas/schemas.py
from datetime import datetime
from http import HTTPStatus
from typing import Optional

from pydantic import BaseModel

class Message(BaseModel):
    message: str
    status: HTTPStatus
    timestamp: datetime
    details: Optional[str] = None

