from typing import List, Optional, Any, Dict
from motor.motor_asyncio import AsyncIOMotorClient
from app.schemas.postal_codes import PostalCodeSchema, PotalCodeSchemaGeoJson
from app.exceptions import NotFoundException
from app.utils.wkb_to_geojson import wkb_to_geojson


class PostalCodeRepository:
    def __init__(self, db: str, collection: str):
        self.db = db
        self.collection = collection

    async def get_by_id(self, db_client: AsyncIOMotorClient, postal_code_id: int) -> PostalCodeSchema:
        result: Optional[Dict[str, Any]] = await db_client[self.db][self.collection].find_one({"id": postal_code_id})
        if not result:
            raise NotFoundException()
        return PostalCodeSchema(**result)

    async def get_with_geojson(self, db_client: AsyncIOMotorClient, postal_code_id: int) -> PotalCodeSchemaGeoJson:
        result: Optional[PostalCodeSchema] = await self.get_by_id(db_client, postal_code_id)
        return PotalCodeSchemaGeoJson(**(result.__dict__), **wkb_to_geojson(result.the_geom))


postal_code_repository = PostalCodeRepository(db="db", collection="postal_codes")
