from enum import Enum
from pydantic import BaseModel


class Role(str, Enum):
    ADMIN = "Администратор"
    USER = "Пользователь"


class UserDto(BaseModel):
    password: str
    login: str
    role: Role
