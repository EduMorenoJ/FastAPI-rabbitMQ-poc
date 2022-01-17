import pytest
import unittest
from httpx import AsyncClient
from app.schemas.paystats import PaystatsSchema
from asyncio import Future
from typing import Final
from app.tests.api.endpoints.test_cases.paystats_tcs import PAYSTATS_GET_ONE_TEST_CASES
from app.exceptions import NotFoundException

PAYSTATS_ID_FOUND: Final[int] = 9999
PAYSTATS_ID_NOT_FOUND: Final[int] = 0000


@pytest.mark.asyncio
async def test_get_paystat_found(mocker, client: AsyncClient, paystat_fixture: PaystatsSchema):

    mock = mocker.patch("app.api.endpoints.paystats.paystats_repository.get_by_id")
    mock.return_value = paystat_fixture
    response = await client.get(f"api/v1/paystats/one/{PAYSTATS_ID_FOUND}")

    assert response.status_code == 200
    assert PaystatsSchema(**response.json()) == paystat_fixture


@pytest.mark.asyncio
async def test_get_paystat_not_found(mocker, client: AsyncClient):

    mocker.patch("app.api.endpoints.paystats.paystats_repository.get_by_id", side_effect=NotFoundException)
    response = await client.get(f"api/v1/paystats/one/{PAYSTATS_ID_NOT_FOUND}")

    assert response.status_code == 404
    assert response.json() is None
