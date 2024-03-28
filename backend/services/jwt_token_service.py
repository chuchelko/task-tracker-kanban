from datetime import datetime, timedelta, timezone
from typing import Optional, Union, Any
from fastapi import HTTPException
from jose import JWTError, jwt

__ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 30 minutes
__REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
__ALGORITHM = "HS256"
__JWT_SECRET_KEY = '20a9bfa73de3f29b6b7a01d4fc84bb569f1b7e8ac7f83c77c62a603f2bf9f5ff' #os.environ['JWT_SECRET_KEY'] <- после докера
__JWT_REFRESH_SECRET_KEY = '20a9bfa73de3f29b6b7a00d4fc84bb569f1b7e8ac7f83c77c62a603f2bf9f5ff' # os.environ['JWT_REFRESH_SECRET_KEY'] <- после докера

def decode_jwt(token: str) -> Optional[dict]:
        try:
            return jwt.decode(token, __JWT_SECRET_KEY, algorithms=[__ALGORITHM], options={"verify_exp": False})
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid token")

def encode_jwt_access(subject: Union[str, Any], expires_delta: int = None) -> str:
    return __create_token(
        subject=subject, 
        expires_delta=expires_delta, 
        secret_key=__JWT_SECRET_KEY,
        expires=__ACCESS_TOKEN_EXPIRE_MINUTES
        )

def encode_jwt_refresh(subject: Union[str, Any], expires_delta: int = None) -> str:
    return __create_token(
        subject=subject,
        expires_delta=expires_delta, 
        secret_key=__JWT_REFRESH_SECRET_KEY,
        expires=__REFRESH_TOKEN_EXPIRE_MINUTES
        )


def __create_token(subject: Union[str, Any], expires_delta: int, secret_key: str, expires: int) -> str:
    if expires_delta is not None:
        expires_delta = datetime.now(timezone.utc) + expires_delta
    else:
        expires_delta = datetime.now(timezone.utc) + timedelta(minutes=expires)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, secret_key, __ALGORITHM)
    return encoded_jwt