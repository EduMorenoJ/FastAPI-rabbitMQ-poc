from typing import List, Optional, Any, Dict
from motor.motor_asyncio import AsyncIOMotorClient
from app.schemas.paystats import PayStatsSchema, TotalAmountByPostalCodeSchema
from app.exceptions import NotFoundException


class PayStatsRepository:
    def __init__(self, db: str, collection: str):
        self.db = db
        self.collection = collection

    async def get_by_id(self, db_client: AsyncIOMotorClient, paystat_id: int) -> PayStatsSchema:
        result: Optional[Dict[str, Any]] = await db_client[self.db][self.collection].find_one({"id": paystat_id})
        if not result:
            raise NotFoundException()
        return PayStatsSchema(**result)

    async def get_by_postal_code(self, db_client: AsyncIOMotorClient, postal_code_id: int) -> List[PayStatsSchema]:
        paystats_by_postal_code: List[PayStatsSchema] = []
        async for doc in db_client[self.db][self.collection].find({"postal_code_id": postal_code_id}):
            paystats_by_postal_code.append(PayStatsSchema(**doc))
        return paystats_by_postal_code

    async def total_amount_grouped_by_postal_code(
        self, db_client: AsyncIOMotorClient
    ) -> List[TotalAmountByPostalCodeSchema]:
        pipeline: List[Dict[str, Any]] = [
            {"$group": {"_id": "$postal_code_id", "total_amount": {"$sum": "$amount"}}},
            {"$project": {"postal_code_id": "$_id", "total_amount": 1}},
        ]
        paystats_total_amount_by_postal_code: List[TotalAmountByPostalCodeSchema] = []
        async for doc in db_client[self.db][self.collection].aggregate(pipeline):
            paystats_total_amount_by_postal_code.append(TotalAmountByPostalCodeSchema(**doc))
        return paystats_total_amount_by_postal_code


paystats_repository: PayStatsRepository = PayStatsRepository(db="db", collection="paystats")
