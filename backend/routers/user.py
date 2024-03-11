from fastapi import APIRouter, Request, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from backend.schemas.userdto import UserDto
from backend.services import user_service
from backend.models import db_helper

router = APIRouter()


@router.post("/create_user")
async def create_user(user: UserDto, db: AsyncSession = Depends(db_helper.session_maker)) -> UserDto:
    return await user_service.create_user(db, user)
