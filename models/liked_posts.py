from models.base import Base
from datetime import datetime
from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey


class LikedPosts(Base):
    __tablename__ = "liked_posts"

    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP, default=datetime.now)
    user_id = Column(
        Integer,  ForeignKey("user.id"), nullable=False, index=True
    )
    post_id = Column(Integer, nullable=False, index=True, unique=True)
