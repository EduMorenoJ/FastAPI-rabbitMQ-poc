from typing import List, Union
from fastapi import Depends, APIRouter
from motor.frameworks import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.responses import JSONResponse
from app.exceptions import NotFoundException
from app.api.responses import NOT_FOUND
from app.schemas.postal_codes import PostalCodeSchema, PotalCodeSchemaGeoJson
from app.db.mongodb import get_client_db
from app.repository.postal_code_repository import postal_code_repository

router = APIRouter()


@router.get(
    "/one/{postal_code_id}",
    response_model=PostalCodeSchema,
    summary="Return one postal code elements",
)
async def get_postal_code(
    postal_code_id: int, db_client: AsyncIOMotorClient = Depends(get_client_db)
) -> Union[PostalCodeSchema, JSONResponse]:
    try:
        result = await postal_code_repository.get_by_id(db_client, postal_code_id)
        return result
    except NotFoundException:
        return NOT_FOUND.response


@router.get(
    "/one/with-geo-json/{postal_code_id}",
    response_model=PotalCodeSchemaGeoJson,
    summary="Return the_geom of a postal code transformed to geojson",
)
async def get_geo_json(
    postal_code_id: int, db_client: AsyncIOMotorClient = Depends(get_client_db)
) -> Union[PostalCodeSchema, JSONResponse]:
    try:
        result = await postal_code_repository.get_with_geojson(db_client, postal_code_id)
        return result
    except NotFoundException:
        return NOT_FOUND.response
