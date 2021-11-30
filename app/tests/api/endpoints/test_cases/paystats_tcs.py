from app.tests.conftest import paystat_fixture
from app.exceptions import NotFoundException

PAYSTATS_GET_ONE_TEST_CASES = {
    "paystats_id_found": {"paystats_id": 9999, "expected_status_code": 200, "expected_result": paystat_fixture},
    "paystats_id_not_found": {"paystats_id": 0000, "expected_status_code": 404, "expected_result": NotFoundException},
}
