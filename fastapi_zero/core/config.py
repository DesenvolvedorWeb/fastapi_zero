# fastapi_zero/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    # Configuração do banco de dados
    DATABASE_URL: str = 'sqlite:///./fastapi_zero.db'  # Exemplo com SQLite local
    # Para produção, use algo como:
    # DATABASE_URL: str = 'postgresql://user:password@localhost/dbname'

    APP_TITLE: str = 'FastAPI Zero'
    DEBUG: bool = True

    # Adicione outras configurações conforme necessário


settings = Settings()
