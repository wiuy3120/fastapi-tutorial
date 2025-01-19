from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from db import Base


class Blog(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey("user.id"))
    author = relationship("User", back_populates="blogs")
    created_at = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=False)
