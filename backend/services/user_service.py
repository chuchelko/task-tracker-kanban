from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.models import User
from backend.schemas.user import UserDto
from backend.repositories.user import UserRepository


async def create_user(
        db: AsyncSession,
        user_data: UserDto,
        user_repository=UserRepository()) -> UserDto:
    return await user_repository.create_user(db=db, user_data=user_data)


async def get_all_users(
        db: AsyncSession,
        user_repository=UserRepository()) -> Sequence[User]:
    return await user_repository.get_all_user(db)


async def get_user_by_id(
        db: AsyncSession,
        id: int,
        user_repository=UserRepository()):
    return await user_repository.det_user_by_id(db, id)
