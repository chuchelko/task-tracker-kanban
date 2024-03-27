from pydantic import BaseModel
from typing import List, Optional



class LabelDto(BaseModel):
    name: str = "test"
    tasks: Optional[List[int]]
