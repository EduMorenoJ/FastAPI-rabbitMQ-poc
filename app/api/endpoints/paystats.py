from typing import List
from fastapi import Depends, APIRouter
from schemas.test import Test
from motor.motor_asyncio import AsyncIOMotorClient
from db.mongodb import get_client_db

router = APIRouter()

@router.get(
    "/all",
    response_model=List[Test],
    summary="return all test elements",
)
async def get_paystats(db_client: AsyncIOMotorClient = Depends(get_client_db)):
    message: List[Test] = await get_docs_from_cursor(db_client)
    return message


async def get_docs_from_cursor(db_client) -> List[Test]:
    cursor = db_client['db']['test'].find({})
    message: List[Test] = []
    async for doc in cursor:
        message.append(Test(**doc))
    return message