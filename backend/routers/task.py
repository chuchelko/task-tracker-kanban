from fastapi import APIRouter, Request, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from backend.schemas.task import TaskDto
from backend.models import db_helper
from backend.services import task_service

router = APIRouter()

@router.post("/task/")
async def create_task(user: TaskDto, db: AsyncSession = Depends(db_helper.get_session)):
    return await task_service.create_task(db, user)
