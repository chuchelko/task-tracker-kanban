from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from backend.schemas.label import LabelDto, LabelTaskDto
from backend.repositories.label import LabelRepository
from backend.repositories.task import TaskRepository

async def create_label(
        db: AsyncSession,
        label_data: LabelDto,
        label_repository=LabelRepository()) -> LabelDto:
    return await label_repository.create_label(label_data, db)


async def get_all_labels_with_tasks(
        db: AsyncSession,
        label_repository=LabelRepository(),
        task_repository=TaskRepository()) -> Sequence[LabelDto]:
    labels = await label_repository.get_all_labels(db)
    labels = [LabelDto(id=x.id, name=x.name, tasks=[]) for x in labels]
    for label in labels:
        tasks = await task_repository.get_all_tasks_by_label_id(db, label.id)
        label.tasks = [LabelTaskDto(id=t.id, name=t.name) for t in tasks]
    return labels
    


async def get_label_by_id(
        db: AsyncSession,
        id: int,
        label_repository=LabelRepository()):
    return await label_repository.get_label_by_id(db, id)
