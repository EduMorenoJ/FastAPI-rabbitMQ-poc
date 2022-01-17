from typing import List, Union
from fastapi import Depends, APIRouter
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.responses import JSONResponse
from app.exceptions import NotFoundException
from app.api.responses import NOT_FOUND
from app.schemas.paystats import PaystatsSchema, TotalAmountByPostalCodeSchema
from app.clients_config.mongodb import get_client_db
from app.repository.paystats_repository import paystats_repository

router = APIRouter()


@router.get(
    "/one/{paystat_id}",
    response_model=PaystatsSchema,
    summary="Return one paysats elements",
)
async def get_paystat(
    paystat_id: int, db_client: AsyncIOMotorClient = Depends(get_client_db)
) -> Union[PaystatsSchema, JSONResponse]:
    try:
        result = await paystats_repository.get_by_id(db_client, paystat_id)
        print(result)
        return result
    except NotFoundException:
        return NOT_FOUND.response


@router.get(
    "/get-by-postal-code/{postal_code_id}",
    response_model=List[PaystatsSchema],
    summary="Return paysats elements by postal code",
)
async def get_paystat_by_postal_code(
    postal_code_id: int, db_client: AsyncIOMotorClient = Depends(get_client_db)
) -> List[PaystatsSchema]:
    return await paystats_repository.get_by_postal_code(db_client, postal_code_id)


@router.get(
    "/total-amount-for-postal-code/",
    response_model=List[TotalAmountByPostalCodeSchema],
    summary="Return total paysats amount by postal code",
)
async def get_paystat_total_amount_grouped_by_postal_code(
    db_client: AsyncIOMotorClient = Depends(get_client_db),
) -> List[TotalAmountByPostalCodeSchema]:
    return await paystats_repository.total_amount_grouped_by_postal_code(
        db_client,
    )


@router.get(
    "/get-total-amount-by-time/",
    summary="Return paysats ordered by time. NOT IMPLEMENTED",
)
async def get_total_amount_by_time(db_client: AsyncIOMotorClient = Depends(get_client_db)):
    return "message: List[PaystatsSchema] = get_many_paystats_timeseries(postal_code_id)"


@router.get(
    "/get-total-amount-by-age-and-gender/",
    summary="Return paysats by postal code grouped by age and gender. NOT IMPLEMENTED",
)
async def get_total_amount_by_age_and_gender(db_client: AsyncIOMotorClient = Depends(get_client_db)):
    return "message: List[PaystatsSchema] = get_paystats_by_age_gender(postal_code_id)"
