from fastapi import FastAPI

from app.api import home

app = FastAPI()

app.include_router(home.router)