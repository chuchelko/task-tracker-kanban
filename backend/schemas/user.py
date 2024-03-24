from enum import Enum
from typing import List
from pydantic import BaseModel


class Role(str, Enum):
    ADMIN = "Администратор"
    USER = "Пользователь"


class UserDto(BaseModel):
    password: str
    login: str
    role: Role


class UserMainInfoDto(BaseModel):
    id: int
    name: str
