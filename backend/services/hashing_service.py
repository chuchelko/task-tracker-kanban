from passlib.context import CryptContext

__password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def _get_hashed_password(password: str) -> str:
    return __password_context.hash(password)


def _verify_password(password: str, hashed_pass: str) -> bool:
    return __password_context.verify(password, hashed_pass)