from pydantic import BaseModel
from typing import Any, List


class PostalCodeSchema(BaseModel):
    the_geom: str
    code: int
    id: int


class PotalCodeSchemaGeoJson(PostalCodeSchema):
    type: str
    coordinates: List[Any]
