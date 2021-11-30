from fastapi import APIRouter
from app.api.endpoints import paystats, load_data, postal_codes

api_router = APIRouter()

api_router.include_router(paystats.router, prefix="/paystats", tags=["Paystats"])
api_router.include_router(postal_codes.router, prefix="/postal-codes", tags=["Postal Codes"])
api_router.include_router(load_data.router, prefix="/load-data", tags=["Load"])
