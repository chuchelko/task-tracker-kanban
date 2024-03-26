from enum import Enum
from typing import Callable
from pydantic import BaseModel, GetCoreSchemaHandler


class Role(str, Enum):
    ADMIN = "Администратор"
    USER = "Пользователь"

class UserCreateDto(BaseModel):
    password: str
    name: str

class UserDto(BaseModel):
    id: int
    password: str
    name: str
    role: Role


class UserMainInfoDto(BaseModel):
    id: int
    name: str
