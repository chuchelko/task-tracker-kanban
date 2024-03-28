from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.models.user import UserRole
from backend.schemas.user import UserCreateDto, UserDto
from backend.models import User
from backend.services.hashing_service import verify_password, get_hashed_password

class UserRepository:
    async def create_user(self, db: AsyncSession, user_data: UserCreateDto):
        existing_user = await db.execute(select(User).filter(User.name == user_data.name))
        if existing_user.scalar() is not None:
            raise ValueError("Пользователь с таким именем уже существует.")
        new_user = User(
            hashed_password=get_hashed_password(user_data.password),
            name=user_data.name,
            user_role=UserRole.USER
        )
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        
    async def get_all_user(self, db: AsyncSession) -> Sequence[User]:
        stmt = select(User).order_by(User.id)
        result = await db.execute(stmt)
        users = result.scalars().all()
        return users

    async def get(self, db: AsyncSession, username, password) -> User:
        user = (await db.execute(select(User).filter(User.name == username))).scalar()
        if(user is None or verify_password(password=password, hashed_pass=user.hashed_password) == False):
            return None
        return user

    async def get_user_by_id(self, db: AsyncSession, user_id: int) -> User | None:
        return await db.get(User, user_id)