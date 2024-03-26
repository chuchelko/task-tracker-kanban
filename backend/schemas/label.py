from pydantic import BaseModel
from typing import List, Optional


class LabelDto(BaseModel):
    name: str
    task_id: Optional[List[int]]
