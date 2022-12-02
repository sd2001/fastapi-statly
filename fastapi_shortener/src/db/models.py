from sqlalchemy import Boolean, Column, Integer, String

from ..config.config import base as Base

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True) ## Autoincrement is default
    key = Column(String, unique=True, index=True)
    target_url = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    topics = Column(String, nullable=True)
    clicks = Column(Integer, default=0)