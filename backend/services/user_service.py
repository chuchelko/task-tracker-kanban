from sqlalchemy.ext.asyncio import AsyncSession
from backend.schemas.user import UserDto
from backend.repositories.user import UserRepository


async def create_user(
        db: AsyncSession,
        user_data: UserDto,
        user_repository = UserRepository()) -> UserDto:
    return await user_repository.create_user(db=db, user_data=user_data)
