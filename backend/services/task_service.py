from sqlalchemy.ext.asyncio import AsyncSession
from backend.schemas.task import TaskCreateDto
from backend.repositories.task import TaskRepository

async def create_task(
        db: AsyncSession,
        task_data: TaskCreateDto,
        task_repository = TaskRepository()) -> TaskCreateDto:
    return await task_repository.create_task(db=db, task_data=task_data)
