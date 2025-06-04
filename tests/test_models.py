from dataclasses import asdict
from datetime import datetime

from sqlalchemy import select

from fastapi_zero.models.models import User


def test_create_user_with_mocked_time(db_session, mock_db_time):
    fixed_time = datetime(2025, 6, 4, 12, 0, 0)
    with mock_db_time(model=User, time=fixed_time):
        user = User(
            username='testuser',
            email='testuser@example.com',
            password='hashedpassword'
        )
        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)
        user = db_session.scalar(
            select(User).where(User.username == 'testuser')
        )
        assert user is not None
        assert user.created_at == fixed_time
        assert asdict(user) == {
            'id': user.id,
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'hashedpassword',
            'created_at': fixed_time,
        }
