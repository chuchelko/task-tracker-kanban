from sqlalchemy import Column, Integer, String, ARRAY, ForeignKey
from sqlalchemy.orm import relationship

from backend.models.base_model import BaseModel


class Label(BaseModel):

    name = Column(String)
    task_id = Column(Integer, ForeignKey("tasks.id"))