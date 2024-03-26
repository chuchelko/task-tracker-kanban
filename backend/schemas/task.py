from pydantic import BaseModel
from typing import List, Optional



class TaskDto(BaseModel):
    id: int
    name: str
    description: Optional[str]
    participants: List[int]
    comments: Optional[List[int]]
    label_id: int

    class Config:
        orm_mode = True


class TaskCreateDto(BaseModel):
    name: str
    participant: int
    label_id: int

    class Config:
        orm_mode = True
