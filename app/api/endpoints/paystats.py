from typing import List
from fastapi import Depends, APIRouter
from schemas.paystats import PayStatsSchema
from motor.motor_asyncio import AsyncIOMotorClient
from db.mongodb import get_client_db

router = APIRouter()

@router.get(
    "/one/{paystat_id}",
    response_model=PayStatsSchema,
    summary="return all paysats elements",
)
async def get_paystats(paystat_id: int, db_client: AsyncIOMotorClient = Depends(get_client_db)):
    message: PayStatsSchema = await get_docs_from_cursor(db_client, paystat_id)
    return message


async def get_docs_from_cursor(db_client, paystat_id) -> PayStatsSchema:
    cursor = await db_client['db']['paystats'].find_one({"id":paystat_id})
    # message: List[PayStatsSchema] = []
    # async for doc in cursor:
    #     message.append(PayStatsSchema(**doc))
    return PayStatsSchema(**cursor)