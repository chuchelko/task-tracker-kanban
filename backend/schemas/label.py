from pydantic import BaseModel
from typing import List


class LabelDto(BaseModel):
    name: str
    task_id: List[int]
