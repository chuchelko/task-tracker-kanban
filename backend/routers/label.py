from fastapi import APIRouter, Request, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from backend.models import db_helper
from backend.schemas.label import LabelDto
from backend.services import label_service

router = APIRouter()


@router.post("/label/")
async def create_label(label: LabelDto, db: AsyncSession = Depends(db_helper.get_session)):
    return await label_service.create_label(db, label)


@router.get("/label/get_all")
async def get_all(db: AsyncSession = Depends(db_helper.get_session)):
    return await label_service.get_all_labels(db)


@router.get("/label/get_by_id")
async def get_by_id(label_id: int, db: AsyncSession = Depends(db_helper.get_session)):
    return await label_service.get_label_by_id(db, label_id)
