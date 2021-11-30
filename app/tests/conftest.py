import os
import pytest
from typing import Any, AsyncGenerator, Dict, Final, Generator, List, Tuple
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from app.schemas.paystats import PaystatsSchema
from datetime import date

os.environ["MONGO_INITDB_HOST"] = "localhost"
os.environ["MONGO_INITDB_PORT"] = "27017"
os.environ["MONGO_INITDB_ROOT_USERNAME"] = "test"
os.environ["MONGO_INITDB_ROOT_PASSWORD"] = "test"
os.environ["RABBIT_HOST"] = "localhost"
os.environ["RABBIT_PORT"] = "5672"
os.environ["RABBIT_USERNAME"] = "test"
os.environ["RABBIT_PASSWORD"] = "test"

from app.main import app


@pytest.fixture()
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test") as ac:
            yield ac


@pytest.fixture()
def paystat_fixture() -> PaystatsSchema:
    return PaystatsSchema(
        amount=1.0, p_month=date.today(), p_age="dummy_age", p_gender="p_age", postal_code_id=0000, id=9999
    )
