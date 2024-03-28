from fastapi.security import OAuth2PasswordBearer
import os 


db_url = os.getenv("DATABASE_URL","postgresql+asyncpg://postgres:postgres@localhost:5432/task_tracker_kanban")
reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/api/user/token",
    scheme_name="JWT"
)