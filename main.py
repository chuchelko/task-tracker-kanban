from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
import os

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

HOST_1 = os.getenv("HOST_1","127.0.0.1")
PORT_1 = os.getenv("PORT_1",8000)
PROXY_HEADERS = os.getenv("PROXY_HEADERS", False)

if __name__ == '__main__':
    uvicorn.run('main:app',host=str(HOST_1),port=int(PORT_1), reload=True,proxy_headers=bool(PROXY_HEADERS))
