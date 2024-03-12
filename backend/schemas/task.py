from pydantic import BaseModel

class TaskDto(BaseModel):
    name: str
