from sqlalchemy import *
from config.database import Base


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    date = Column(DateTime, nullable=False)

from sqlalchemy.orm import relationship

class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    date = Column(DateTime, nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"), nullable=False)
    post = relationship("Post", backref="comments")

