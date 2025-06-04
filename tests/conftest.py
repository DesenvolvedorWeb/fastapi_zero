import base64
from contextlib import contextmanager
from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

from fastapi_zero.main import app
from fastapi_zero.models.models import table_registry

DATABASE_URL = 'sqlite:///:memory:'


def get_auth_header(username: str, password: str) -> dict:
    credentials = f'{username}:{password}'
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    return {'Authorization': f'Basic {encoded_credentials}'}


@pytest.fixture
def client():
    headers = get_auth_header('admin', 'fastapizero')
    return TestClient(app, headers=headers)


@pytest.fixture(scope='module')
def engine():
    engine = create_engine(DATABASE_URL, echo=False)
    table_registry.metadata.create_all(bind=engine)
    yield engine
    table_registry.metadata.drop_all(bind=engine)


@pytest.fixture
def db_session(engine):
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = session_local()
    yield session
    session.close()


@pytest.fixture
def mock_db_time():
    @contextmanager
    def _mock_db_time(*, model, time: datetime):
        def fake_time_hook(mapper, connection, target):
            if hasattr(target, 'created_at'):
                target.created_at = time

        event.listen(model, 'before_insert', fake_time_hook)
        try:
            yield time
        finally:
            event.remove(model, 'before_insert', fake_time_hook)

    return _mock_db_time
