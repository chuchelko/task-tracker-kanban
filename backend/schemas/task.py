from enum import Enum
from typing import List
from pydantic import BaseModel
from backend.models.user import User

class TaskLabel(str, Enum):
    HIGHT_PRIORITY = "Высокий приоритет"
    LOW_PRIORITY = "Низкий приоритет"
    IN_WORK = "В работе"
    CODE_REVIEW = "Код ревью"
    CREATED = "Создана"

class Task(BaseModel):
    name: str
    description: str
    reviewers: List[User]
    owners: List[User]
    subscribers: List[User]
    comments: List[str]
    labels: List[TaskLabel]
