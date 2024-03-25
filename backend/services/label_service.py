from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from backend.schemas.label import LabelDto
from backend.repositories.label import LabelRepository


async def create_label(
        db: AsyncSession,
        label_data: LabelDto,
        label_repository=LabelRepository()) -> LabelDto:
    return await label_repository.create_label(label_data, db)


async def get_all_labels(
        db: AsyncSession,
        label_repository=LabelRepository()) -> Sequence[LabelDto]:
    return await label_repository.get_all_labels(db)


async def get_label_by_id(
        db: AsyncSession,
        id: int,
        label_repository=LabelRepository()):
    return await label_repository.get_label_by_id(db, id)
