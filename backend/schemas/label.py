from pydantic import BaseModel
from typing import List, Optional

class LabelTaskDto(BaseModel):
    id: int
    name: str

class LabelDto(BaseModel):
    id: int
    name: str = "test"
    tasks: Optional[List[LabelTaskDto]]
