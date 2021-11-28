import os
from typing import AsyncGenerator
from asyncio import AbstractEventLoop
from aio_pika import connect_robust, Channel, Connection

RABBIT_HOST: str = os.environ["RABBIT_INITDB_HOST"]
RABBIT_PORT: int = int(os.environ["RABBIT_INITDB_PORT"])
RABBIT_USER: str = os.environ["RABBIT_INITDB_ROOT_USERNAME"]
RABBIT_PASSWORD: str = os.environ["RABBIT_INITDB_ROOT_PASSWORD"]

async def get_async_client(
    host: str = RABBIT_HOST, port: int = RABBIT_PORT, username: str = RABBIT_USER, password: str = RABBIT_PASSWORD, loop: AbstractEventLoop = None
) -> Connection:
    return await connect_robust(
            f"amqp://{username}:{password}@{host}:{port}/", loop=loop
        )


async def get_channel_rb() -> AsyncGenerator[Channel, None]:
    try:
        rb_client = await get_async_client()
        channel = await rb_client.channel() 
        yield channel
    finally:
        await rb_client.close()