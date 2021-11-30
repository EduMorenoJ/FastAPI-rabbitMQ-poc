import os
import asyncio
import logging
from asyncio.queues import Queue
import pandas as pd
from typing import Union, Final
from aio_pika.channel import Channel
from motor.motor_asyncio import AsyncIOMotorClient
from aio_pika import IncomingMessage, Connection
from asyncio import AbstractEventLoop
from db.rabbitmq import get_async_client as rabbit_client
from db.mongodb import get_async_client as mongo_client

PATH_TO_CSV: Final[str] = os.environ.get("PATH_TO_CSV", "./data")
DB_NAME: Final[str] = os.environ.get("DB_NAME", "db")


async def load_csv_to_mongo(entity: str, client: AsyncIOMotorClient) -> None:
    try:
        file: str = f"{PATH_TO_CSV}/{entity}.csv"
        with pd.read_csv(file, chunksize=10000) as reader:
            for chunk in reader:
                await client[DB_NAME][entity].insert_many(chunk.to_dict("records"))
        logging.info("File {file} loaded correctly")
    except FileNotFoundError:
        logging.error(f"File {file} not found")
    except Exception as e:
        logging.error(
            f"Exception loading csv data to mongo: {e}",
        )


async def set_queue(loop: AbstractEventLoop) -> Connection:
    connection: Connection = await rabbit_client(loop=loop)
    channel: Channel = await connection.channel()
    queue: Queue = await channel.declare_queue(name="task_queue", durable=True)
    await queue.consume(on_message)
    return connection


async def on_message(message: IncomingMessage) -> None:
    async with message.process():
        client: AsyncIOMotorClient = mongo_client()
        entity: str = message.body.decode("utf-8")
        await load_csv_to_mongo(entity, client)


if __name__ == "__main__":
    loop: AbstractEventLoop = asyncio.get_event_loop()
    connection: Connection = loop.run_until_complete(set_queue(loop))
    try:
        loop.run_forever()
    finally:
        loop.run_until_complete(connection.close())
