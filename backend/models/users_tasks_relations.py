from sqlalchemy import Column, ForeignKey, Integer

from backend.models.base_model import BaseModel

class Reviewer_Task(BaseModel):
    user_id = Column(Integer(), ForeignKey('users.id'))
    task_id = Column(Integer(), ForeignKey('tasks.id'))

class Owner_Task(BaseModel):
    user_id = Column(Integer(), ForeignKey('users.id'))
    task_id = Column(Integer(), ForeignKey('tasks.id'))

class Subscriber_Task(BaseModel):
    user_id = Column(Integer(), ForeignKey('users.id'))
    task_id = Column(Integer(), ForeignKey('tasks.id'))
