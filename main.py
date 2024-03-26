from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

from backend.models import BaseModel, db_helper

from backend.app_initializer import initialize_routes, add_cors_middleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
initialize_routes(app)
add_cors_middleware(app)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
