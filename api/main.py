from fastapi import FastAPI
from .routers import ping

api = FastAPI()
api.include_router(ping.router)
