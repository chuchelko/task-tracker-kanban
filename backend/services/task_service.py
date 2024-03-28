from sqlalchemy.ext.asyncio import AsyncSession

from backend.models import Task
from backend.repositories.label import LabelRepository
from backend.schemas.task import (
    TaskCreateDto,
    TaskDto,
    TaskUpdateCommentDto,
    TaskUpdateDto,
    TaskUpdateParticipantDto,
)
from backend.repositories.task import TaskRepository


async def create_task(
    db: AsyncSession, task_data: TaskCreateDto, user_id: int, task_repository=TaskRepository()
):
    return await task_repository.create_task(db=db, task_data=task_data, user_id=user_id)


async def update_task(
    db: AsyncSession, task_data: TaskUpdateDto, task_repository=TaskRepository()
):
    return await task_repository.update_task(db=db, task_data=task_data)


async def get_task(db: AsyncSession, id: int, task_repository=TaskRepository()):
    task = await task_repository.get_task(db, id)
    taskupd = TaskUpdateDto(
        id=task.id,
        name=task.name,
        label_id=task.label_id,
        description=task.description,
        participants=[
            TaskUpdateParticipantDto(id=p.id, name=p.name) for p in task.participants
        ],
        comments=[
            TaskUpdateCommentDto(user_id=c.user_id, text=c.text) for c in task.comments
        ],
    )
    return taskupd