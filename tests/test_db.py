from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from app.models.models import User, table_registry


def test_create_user(session):    
    user = User(
        username='silva',
        email='silv@mail.com',
        password='mysenha',
    )
    session.add(user)
    session.commit()
    # session.refresh(user)

    result = session.scalar(
        select(User).where(User.email == 'silv@mail.com')
    )

    assert result.username == 'silva'
