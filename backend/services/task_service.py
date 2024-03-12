from sqlalchemy.ext.asyncio import AsyncSession
from backend.schemas.task import TaskDto
from backend.repositories.task import TaskRepository

async def create_task(
        db: AsyncSession,
        task_data: TaskDto,
        task_repository = TaskRepository()) -> TaskDto:
    return await task_repository.create_task(db=db, task_data=task_data)
