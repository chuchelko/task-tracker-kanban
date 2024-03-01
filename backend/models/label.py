from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ENUM as PgEnum

from backend.models.base_model import BaseModel

class Label(BaseModel):
    name = Column(String)