from typing import Final, Dict, Union, Any
from fastapi.responses import JSONResponse

from pydantic import BaseModel

class APIResponse(BaseModel):
    openapi_info: Dict[Union[int, str], Dict[str, Any]]
    response: JSONResponse
    class Config:
        arbitrary_types_allowed = True


SERVER_ERROR: Final[APIResponse] = APIResponse(
    openapi_info={500: {'model': {'description': 'Unexpected Error'}}},
    response=JSONResponse(status_code=500),
)

LOAD_STARTED: Final[APIResponse] = APIResponse(
    openapi_info={201: {'load': 'message sent to persistor'}},
    response=JSONResponse(status_code=201,content='Message sent to persistor'),


)