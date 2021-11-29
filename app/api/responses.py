from typing import Final
from fastapi.responses import JSONResponse

from app.schemas.api_responses import APIResponse

SERVER_ERROR: Final[APIResponse] = APIResponse(
    openapi_info={500: {"model": {"description": "Unexpected Error"}}},
    response=JSONResponse(status_code=500),
)

LOAD_STARTED: Final[APIResponse] = APIResponse(
    openapi_info={201: {"load": "message sent to persistor"}},
    response=JSONResponse(status_code=201, content="Message sent to persistor"),
)

NOT_FOUND: Final[APIResponse] = APIResponse(
    openapi_info={404: {"model": None}},
    response=JSONResponse(status_code=404),
)
