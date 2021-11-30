from typing import Dict, Any
from shapely import wkb


def wkb_to_geojson(wkb_to_convert: str) -> Dict[str, Any]:
    return wkb.loads(wkb_to_convert, hex=True).__geo_interface__
