from pydantic import BaseModel
from typing import Dict, Any, List, Tuple


class PostalCodeSchema(BaseModel):
    the_geom: str
    code: int
    id: int


class PotalCodeSchemaGeoJson(PostalCodeSchema):
    type: str
    coordinates: List[Tuple[Any]]
