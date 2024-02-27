from fastapi import FastAPI, Form
import uvicorn

from backend.app_initializer import initialize_routes

app = FastAPI()
initialize_routes(app)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
