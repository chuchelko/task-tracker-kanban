from pydantic import BaseModel
from typing import List, Optional

from backend.models.task import TaskLabel

class TaskDto(BaseModel):
    id: int
    name: str
    description: Optional[str]
    participants: List[int]
    comments: Optional[List[int]]
    label: TaskLabel

class TaskCreateDto(BaseModel):
    name: str
    participant: int
    label: TaskLabel