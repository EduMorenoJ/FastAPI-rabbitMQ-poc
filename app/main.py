from typing import Final
import uvicorn
from fastapi import FastAPI
from api.api_routes import api_router

API_V: Final[str] = "/api/v1"

app = FastAPI(
    title="My awesome API",
    openapi_url=f"{API_V}/openapi.json")
    
app.include_router(api_router, prefix=API_V)

# @app.get("/")
# async def root(db_client: AsyncIOMotorClient = Depends(get_client_db)):
#     message = await get_docs_from_cursor(db_client)
#     return {"message": message}

# async def get_docs_from_cursor(db_client):
#     cursor = db_client['db']['test'].find({})
#     message = []
#     async for doc in cursor:
#         message.append(Test(**doc))
#     return message

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)