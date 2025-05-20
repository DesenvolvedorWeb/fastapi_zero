import base64

import pytest
from fastapi.testclient import TestClient

from fastapi_zero.main import app


def get_auth_header(username: str, password: str) -> dict:
    credentials = f'{username}:{password}'
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    return {'Authorization': f'Basic {encoded_credentials}'}


@pytest.fixture
def client():
    headers = get_auth_header('admin', 'fastapizero')
    return TestClient(app, headers=headers)
