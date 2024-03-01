from fastapi import FastAPI

from backend.routers import user, task

prefix = "/api"

def initialize_routes(app: FastAPI):
    app.include_router(user.router, prefix=prefix)
    app.include_router(task.router, prefix=prefix)