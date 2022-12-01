from fastapi import APIRouter
from api.dependencies import API_NAME


router = APIRouter(prefix="/ping")


@router.get("")
def ping():
    return {API_NAME: "pong"}