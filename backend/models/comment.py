from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import ENUM as PgEnum

from backend.models.base_model import BaseModel

class Comment(BaseModel):
    text = Column(String(500))
    user_id = Column(Integer, ForeignKey('users.id'))