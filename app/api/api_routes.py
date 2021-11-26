from fastapi import APIRouter
from api.endpoints import paystats, files

api_router = APIRouter()

api_router.include_router(paystats.router, prefix="/paystats", tags=["paystats"])
api_router.include_router(files.router, prefix="/files", tags=["files"])
