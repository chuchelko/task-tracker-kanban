from sqlalchemy.ext.asyncio import AsyncSession
from backend.schemas.userdto import UserDto
from backend.repositories.user import UserRepository


async def create_user(db: AsyncSession, user_data: UserDto) -> UserDto:
    return await UserRepository.create_user(db, user_data)
