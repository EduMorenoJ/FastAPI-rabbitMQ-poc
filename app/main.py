from typing import Final
import uvicorn
from fastapi import FastAPI
from app.api.api_routes import api_router

API_V: Final[str] = "/api/v1"

app = FastAPI(title="My awesome API", openapi_url=f"{API_V}/openapi.json")

app.include_router(api_router, prefix=API_V)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
