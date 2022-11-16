from fastapi import FastAPI
from api.dependencies import API_NAME
from api.routers import ping


BASE_ROUTE = f'/{API_NAME.lower()}'


api = FastAPI()
api.include_router(ping.router, prefix=BASE_ROUTE)
