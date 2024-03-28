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

class TaskUpdateCommentDto(BaseModel):
    user_id: int
    text: str

class TaskUpdateParticipantDto(BaseModel):
    id: int | None
    name: str | None
    
class TaskUpdateDto(BaseModel):
    id: int
    name: Optional[str] = None
    label_id: Optional[int] = None
    description: Optional[str] = None
    participants: Optional[List[TaskUpdateParticipantDto]] = None
    comments: Optional[List[TaskUpdateCommentDto]] = None

class TaskCreateDto(BaseModel):
    name: str
    participant: int
    label_id: int

    class Config:
        orm_mode = True
