import pytest
import unittest
from httpx import AsyncClient
from app.schemas.paystats import PayStatsSchema

PAYSTATS_ID = 9999


# @pytest.mark.asyncio
# async def test_get_paystat(mocker, client: AsyncClient, paystat_fixture: PayStatsSchema):
#     async def task_from_result(result):
#         return result

#     # mock = unittest.mock.MagicMock()
#     # mock.app.repository.paystats_repository.PayStatsRepository.get_by_id.return_value = task_from_result(
#     #     paystat_fixture
#     # )
#     mock = mocker.patch(
#         "app.api.endpoints.paystats.paystats_repository.get_by_id",
#         return_value=task_from_result(paystat_fixture),
#     )
#     response = await client.get(f"api/v1/paystats/one{PAYSTATS_ID}")
#     # mock_kwargs = mock_read.call_args.kwargs

#     # assert mock_kwargs["filter"] == {"state": LoadState.success}
#     # assert mock_kwargs["sort"] == [("start_date", DESCENDING)]
#     assert response.status_code == 200
#     assert response.json() == paystat_fixture


from app.api.endpoints.paystats import get_paystat
from app.db.mongodb import get_client_db


@pytest.mark.asyncio
async def test_get_paystats(mocker, client: AsyncClient, paystat_fixture: PayStatsSchema):
    mock = mocker.patch(
        "app.api.endpoints.paystats.paystats_repository.get_by_id",
        return_value=paystat_fixture,
    )

    r = get_paystat(9999, get_client_db())
