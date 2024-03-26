from sqlalchemy.ext.asyncio import AsyncSession

from backend.models import Task
from backend.repositories.label import LabelRepository
from backend.schemas.task import TaskCreateDto
from backend.repositories.task import TaskRepository

async def create_task(
        db: AsyncSession,
        task_data: TaskCreateDto,
        label_repository = LabelRepository(),
        task_repository = TaskRepository()) -> Task:
    label = await label_repository.get_label_by_id(db, task_data.label_id)
    if label:
        await label_repository.update_label(label, db)
    return await task_repository.create_task(db=db, task_data=task_data)
