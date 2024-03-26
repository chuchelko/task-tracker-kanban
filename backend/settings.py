from fastapi.security import OAuth2PasswordBearer


db_url = "postgresql+asyncpg://postgres:postgres@localhost:5432/task_tracker_kanban"
reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/api/user/token",
    scheme_name="JWT"
)