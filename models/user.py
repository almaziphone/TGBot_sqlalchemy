from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Sequence, Boolean

from .base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String)
    username = Column(String, default=None)
    language = Column(String, default='en')

    is_admin = Column(Boolean, default=False)

    created_at = Column(DateTime, default=lambda: datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self) -> str:
        return f'<User {self.username}>'
