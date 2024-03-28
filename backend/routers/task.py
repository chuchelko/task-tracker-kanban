from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from backend.schemas.task import TaskCreateDto, TaskUpdateDto
from backend.models import db_helper
from backend.services import task_service
from backend.services.authorization_service import authorize_user
from backend.settings import reuseable_oauth

router = APIRouter()


@router.post("/task/")
async def create_task(
    task: TaskCreateDto,
    token: str = Depends(reuseable_oauth),
    db: AsyncSession = Depends(db_helper.get_session),
):
    user_id = await authorize_user(token, db)
    return await task_service.create_task(db, task, user_id)


@router.put("/task/")
async def update_task(
    task: TaskUpdateDto,
    token: str = Depends(reuseable_oauth),
    db: AsyncSession = Depends(db_helper.get_session),
):
    await authorize_user(token, db)
    try:
        return await task_service.update_task(db, task)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/task/{id}")
async def get_task_info(
    id: int,
    token: str = Depends(reuseable_oauth),
    db: AsyncSession = Depends(db_helper.get_session),
):
    await authorize_user(token, db)
    try:
        task = await task_service.get_task(db, id)
        print('бля', task)
        return task
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
