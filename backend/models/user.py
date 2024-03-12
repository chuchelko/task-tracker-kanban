from enum import Enum
from sqlalchemy import Column, Integer, String, Enum as SqlEnum
from sqlalchemy.orm import relationship

from backend.models.base_model import BaseModel

class UserRole(Enum):
    ADMIN = 'admin'
    USER = 'user'

class User(BaseModel):
    hashed_password = Column(String)
    name = Column(String(20))
    user_role = Column(SqlEnum(UserRole))
    tasks_owner = relationship('Owner_Task', backref='user', primaryjoin='User.id == Owner_Task.user_id')
    tasks_subscriber = relationship('Subscriber_Task', backref='user', primaryjoin='User.id == Subscriber_Task.user_id')
    comments = relationship('Comment', primaryjoin='User.id == Comment.user_id')