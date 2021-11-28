import json
from enum import Enum
from fastapi import Depends, APIRouter
from aio_pika import Channel, Message, DeliveryMode
from db.rabbitmq import get_channel_rb
from api.responses import SERVER_ERROR, LOAD_STARTED
# @router.post("/startLoad/")
# async def create_upload_files(file: UploadFile = File(...)):
#     return {"filenames": file.filename}

router = APIRouter()

class AllowedEntities(str, Enum):
    paystats = "paystats"
    postal_codes = "postal_codes"

@router.post("/loadEntity/")
async def create_upload_files(entity: AllowedEntities,channel:Channel = Depends(get_channel_rb)):
    try:
        await channel.default_exchange.publish(
            Message(
                body=entity.encode(),
                delivery_mode=DeliveryMode.PERSISTENT
            ),
            routing_key="task_queue"
        )
        return LOAD_STARTED.response
    except Exception as e:
        return SERVER_ERROR.response