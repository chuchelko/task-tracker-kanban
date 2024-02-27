from enum import Enum
from pydantic import BaseModel

class UserRole(Enum):
    ADMIN = 1
    USER = 2

class UserPostDto(BaseModel):
    password: int
    login: int
    role: UserRole