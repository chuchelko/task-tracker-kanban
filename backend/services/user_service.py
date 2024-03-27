from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.models import User
from backend.schemas.user import Role, UserCreateDto, UserDto, UserMainInfoDto
from backend.repositories.user import UserRepository

def _get_role(user_role)->Role:
    return Role[str(user_role).split('.')[1].upper()]

async def create_user(
    db: AsyncSession, user_data: UserCreateDto, user_repository=UserRepository()
):
    await user_repository.create_user(db=db, user_data=user_data)


async def get_all_users(
    db: AsyncSession, user_repository=UserRepository()
) -> Sequence[UserMainInfoDto]:
    users = await user_repository.get_all_user(db)
    return [UserMainInfoDto(id=x.id, name=x.name, role=_get_role(x.user_role)) for x in users]


async def get_main_info(id: int, db: AsyncSession, user_repository=UserRepository()):
    user = await user_repository.get_user_by_id(db=db, user_id=id)
    return UserMainInfoDto(id=user.id, name=user.name, role=_get_role(user.user_role))


async def get(
    db: AsyncSession, username: str, password: str, user_repository=UserRepository()
) -> UserDto:
    user = await user_repository.get(db, username, password)
    if user is None:
        return None
    return UserDto(
        id=user.id,
        password=password,
        name=username,
        role=_get_role(user.user_role)
        )
