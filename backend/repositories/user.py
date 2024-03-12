from sqlalchemy.ext.asyncio import AsyncSession
from backend.models.user import UserRole
from backend.schemas.user import UserDto
from backend.models import User


class UserRepository:
    async def create_user(self, db: AsyncSession, user_data: UserDto) -> User:
        new_user = User(
            hashed_password = user_data.password + 'hash)))',
            name = user_data.login,
            user_role = UserRole.USER
        )
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return new_user
