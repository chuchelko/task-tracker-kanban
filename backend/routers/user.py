from fastapi import APIRouter, Request

from backend.schemas.user import User
from backend.services import user_service

router = APIRouter()

@router.post("/users/")
async def post_user(user: User):
    user_service.create_user(user)