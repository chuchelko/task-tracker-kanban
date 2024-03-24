from fastapi import APIRouter, Request, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from backend.schemas.user import UserDto
from backend.services import user_service
from backend.models import db_helper

router = APIRouter()


@router.post("/user/")
async def create_user(user: UserDto, db: AsyncSession = Depends(db_helper.get_session)):
    return await user_service.create_user(db, user)


@router.get("/user/get_all")
async def get_all(db: AsyncSession = Depends(db_helper.get_session)):
    return await user_service.get_all_users(db)


@router.get("/user/get_by_id")
async def get_by_id(user_id: int, db: AsyncSession = Depends(db_helper.get_session)):
    return await user_service.get_user_by_id(db, user_id)
