# fastapi_zero/core/security.py
import secrets
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

# Configuração de segurança
security = HTTPBasic(realm='FastAPI Zero API')

# Credenciais de exemplo (em produção, use banco de dados)
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'fastapizero'


def get_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    """
    Verifica as credenciais do usuário usando comparação segura.
    Retorna o nome de usuário se as credenciais forem válidas.
    """
    # Converte para bytes para comparação segura
    current_username_bytes = credentials.username.encode('utf8')
    correct_username_bytes = ADMIN_USERNAME.encode('utf8')

    current_password_bytes = credentials.password.encode('utf8')
    correct_password_bytes = ADMIN_PASSWORD.encode('utf8')

    # Usa secrets.compare_digest para evitar timing attacks
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )

    # Se as credenciais não forem válidas, lança exceção
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Credenciais inválidas',
            headers={'WWW-Authenticate': 'Basic'},
        )

    return credentials.username
