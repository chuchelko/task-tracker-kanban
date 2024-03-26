import re
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timezone

from fastapi import HTTPException
from jose import JWTError
from backend.services.jwt_token_service import decode_jwt
from backend.services import user_service


async def authorize_user(token: str, db: AsyncSession):
    try:
        payload = decode_jwt(token)
        print(payload)
        if payload.get("exp") < datetime.now(timezone.utc).timestamp():
            raise HTTPException(
                    status_code = status.HTTP_401_UNAUTHORIZED,
                    detail="Token expired",
                    headers={"WWW-Authenticate": "Bearer"},
                )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    sub = payload.get("sub")
    userid = int(re.search(r"id=(\d+)", sub).group(1))
    return await user_service.get_main_info(id=userid, db=db)