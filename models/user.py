from datetime import datetime
from models.base import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, UniqueConstraint


class User(Base):
    __tablename__ = "user"

    # table columns and data types
    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP, default=datetime.now)
    username = Column(String(20), index=True, unique=True)
    short_description = Column(String)
    long_bio = Column(String)
    # email, password
