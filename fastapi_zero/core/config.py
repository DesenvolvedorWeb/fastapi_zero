
# fastapi_zero/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_TITLE: str = "FastAPI Zero"
    DEBUG: bool = True

    # Adicione outras configurações conforme necessário

    class Config:
        env_file = ".env"

settings = Settings()

