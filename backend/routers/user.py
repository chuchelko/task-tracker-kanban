from fastapi import APIRouter, HTTPException, Depends, status

from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from backend.schemas.user import UserCreateDto, UserMainInfoDto
from backend.services import user_service
from backend.models import db_helper
from backend.services.authorization_service import authorize_user
from backend.services.jwt_token_service import encode_jwt_access, encode_jwt_refresh
from backend.settings import reuseable_oauth

router = APIRouter()

@router.post("/user/")
async def create(user: UserCreateDto, db: AsyncSession = Depends(db_helper.get_session)):
    try:
        await user_service.create_user(db, user)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get("/users")
async def get_all(db: AsyncSession = Depends(db_helper.get_session)):
    return await user_service.get_all_users(db)

@router.post("/user/token")
async def login_user_get_token(
        form_data: UserCreateDto,
        db: AsyncSession = Depends(db_helper.get_session)
    ):
    user = await user_service.get(db, form_data.name, form_data.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Некорректные данные"
        )
    return {
        "access_token": encode_jwt_access(user),
        "refresh_token": encode_jwt_refresh(user),
    }

@router.get("/user")
async def get_by_token(
    db: AsyncSession = Depends(db_helper.get_session),
    token: str = Depends(reuseable_oauth)
    ) -> UserMainInfoDto:
    return await authorize_user(token=token, db=db)
