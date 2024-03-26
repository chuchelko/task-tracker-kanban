from sqlalchemy import Column, ForeignKey, Integer

from backend.models.base_model import BaseModel

class Label_Task(BaseModel):
    label_id = Column(Integer(), ForeignKey('labels.id'))
    task_id = Column(Integer(), ForeignKey('tasks.id'))