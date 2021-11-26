import os
from typing import AsyncGenerator
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_HOST: str = os.environ["MONGO_INITDB_HOST"]
MONGO_PORT: int = int(os.environ["MONGO_INITDB_PORT"])
MONGO_USER: str = os.environ["MONGO_INITDB_ROOT_USERNAME"]
MONGO_PASSWORD: str = os.environ["MONGO_INITDB_ROOT_PASSWORD"]


def get_async_client(
    host: str = MONGO_HOST, port: int = MONGO_PORT, username: str = MONGO_USER, password: str = MONGO_PASSWORD
) -> AsyncIOMotorClient:
    return AsyncIOMotorClient(host=host, port=port, username=username, password=password)


async def get_client_db() -> AsyncGenerator[AsyncIOMotorClient, None]:
    db_client: AsyncIOMotorClient = get_async_client()
    try:
        yield db_client
    finally:
        db_client.close()
