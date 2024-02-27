from fastapi import FastAPI

from backend.infrastructure.routers import users_router

prefix = "/api"

def initialize_routes(app: FastAPI):
    app.include_router(users_router.router, prefix=prefix)