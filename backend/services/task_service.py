from sqlalchemy.ext.asyncio import AsyncSession

from backend.models import Task
from backend.repositories.label import LabelRepository
from backend.schemas.task import TaskCreateDto, TaskDto, TaskUpdateDto
from backend.repositories.task import TaskRepository

async def create_task(
        db: AsyncSession,
        task_data: TaskCreateDto,
        task_repository = TaskRepository()):
    return await task_repository.create_task(db=db, task_data=task_data)

async def update_task(
        db: AsyncSession,
        task_data: TaskUpdateDto,
        task_repository = TaskRepository()):
    return await task_repository.update_task(db=db, task_data=task_data)
