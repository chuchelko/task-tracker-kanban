from fastapi import APIRouter, Request

from backend.infrastructure.dto.user_post_dto import UserPostDto


router = APIRouter()

@router.post("/users/")
async def post_user(user: UserPostDto):
    print(user)