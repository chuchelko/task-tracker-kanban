from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.models import Label
from backend.schemas.label import LabelDto


class LabelRepository:
    async def create_label(self, label_dto: LabelDto, db: AsyncSession) -> LabelDto:
        label = Label(name=label_dto.name)
        db.add(label)
        await db.commit()
        await db.refresh(label)
        return label_dto

    async def get_all_labels(self, db: AsyncSession) -> Sequence[Label]:
        stmt = select(Label).order_by(Label.id)
        result = await db.execute(stmt)
        return result.scalars().all()

    async def get_label_by_id(self, db: AsyncSession, label_id: int) -> Label | None:
        return await db.get(Label, label_id)
