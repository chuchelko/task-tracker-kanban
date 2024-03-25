from typing import Optional
from sqlalchemy import Column, Integer, String, ForeignKey
from enum import Enum
from sqlalchemy.dialects.postgresql import ENUM as PgEnum
from sqlalchemy.orm import relationship

from backend.models.base_model import BaseModel

class TaskLabel(str, Enum):
    CREATED = "Создана"
    IN_WORK = "В работе"
    CODE_REVIEW = "Код ревью"
    TESTING = "Тестирование"
    READY   = "Готова"


class Task(BaseModel):
    name = Column(String(100))
    description = Column(String(500))
    participants = relationship('Participant_Task', backref='task', primaryjoin='Task.id == Participant_Task.task_id')
    comments = relationship('Comment', backref='task', primaryjoin='Task.id == Comment.task_id')
    label = relationship('Label', backref='task', primaryjoin='Task.id == Label.task_id')