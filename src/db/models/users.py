from sqlalchemy import (
    Column,
    Integer,
    String,
)
from ..base_class import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    password_hash = Column(String)
    first_name = Column(String)
    last_name = Column(String)
