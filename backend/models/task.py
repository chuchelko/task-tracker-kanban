from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ENUM as PgEnum
from sqlalchemy.orm import relationship

from backend.models.base_model import BaseModel

class Task(BaseModel):
    name = Column(String(100))
    description = Column(String(500))
    reviewers = relationship('Reviewer_Task', backref='task')
    owners = relationship('Owner_Task', backref='task')
    subscribers = relationship('Subscriber_Task', backref='task')
    comments = relationship('Comment', backref='task')
    labels = relationship('Label', backref='task')