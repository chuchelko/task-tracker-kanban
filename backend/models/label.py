from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from backend.models.base_model import BaseModel


class Label(BaseModel):
    name = Column(String)
    task = relationship("Task", primaryjoin='Label.id == Task.label_id')

    class Config:
        arbitrary_types_allowed = True