from sqlalchemy import Column, ForeignKey, Integer

from backend.models.base_model import BaseModel

class Participant_Task(BaseModel):
    user_id = Column(Integer(), ForeignKey('users.id'))
    task_id = Column(Integer(), ForeignKey('tasks.id'))
