from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routers import user, task, label

prefix = "/api"


def initialize_routes(app: FastAPI):
    app.include_router(user.router, prefix=prefix)
    app.include_router(task.router, prefix=prefix)
    app.include_router(label.router, prefix=prefix)
    
def add_cors_middleware(app: FastAPI):
    origins = [
    "http://localhost",
    "http://localhost:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
