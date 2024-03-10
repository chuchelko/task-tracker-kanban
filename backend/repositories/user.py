from sqlalchemy.ext.asyncio import AsyncSession
from backend.schemas.userdto import UserDto
from backend.models import User


class UserRepository:
    async def create_user(self, db: AsyncSession, user_data: UserDto) -> User:
        new_user = User(user_data.password, user_data.login, user_data.role)
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return new_user
