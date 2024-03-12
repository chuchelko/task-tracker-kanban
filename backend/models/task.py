from sqlalchemy import Column, Integer, String
from enum import Enum
from sqlalchemy.dialects.postgresql import ENUM as PgEnum
from sqlalchemy.orm import relationship

from backend.models.base_model import BaseModel

class TaskLabel(str, Enum):
    HIGHT_PRIORITY = "Высокий приоритет"
    LOW_PRIORITY = "Низкий приоритет"
    IN_WORK = "В работе"
    CODE_REVIEW = "Код ревью"
    CREATED = "Создана"


class Task(BaseModel):
    name = Column(String(100))
    description = Column(String(500))
    reviewers = relationship('Reviewer_Task', backref='task', primaryjoin='Task.id == Reviewer_Task.task_id')
    owners = relationship('Owner_Task', backref='task', primaryjoin='Task.id == Owner_Task.task_id')
    subscribers = relationship('Subscriber_Task', backref='task', primaryjoin='Task.id == Subscriber_Task.task_id')
    comments = relationship('Comment', backref='task', primaryjoin='Task.id == Comment.task_id')
    labels = relationship('Label', backref='task', primaryjoin='Task.id == Label.task_id')