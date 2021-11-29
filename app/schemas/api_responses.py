from pydantic import BaseModel
from typing import Dict, Union, Any
from fastapi.responses import JSONResponse


class APIResponse(BaseModel):
    openapi_info: Dict[Union[int, str], Dict[str, Any]]
    response: JSONResponse

    class Config:
        arbitrary_types_allowed = True
