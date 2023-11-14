import pytest

from api.forms.validators import (
    validate_date,
    validate_email,
    validate_phone,
)
from tests.unit.forms.parametrize_data import (
    date_examples,
    email_examples,
    phone_example,
)


@pytest.mark.unit
@pytest.mark.parametrize(
    'data, expected_result',
    phone_example,
    ids=str,
)
def test_validate_phone(data: str, expected_result: bool) -> None:
    assert validate_phone(data) == expected_result


@pytest.mark.unit
@pytest.mark.parametrize(
    'data, expected_result',
    date_examples,
    ids=str,
)
def test_validate_date(data: str, expected_result: bool) -> None:
    assert validate_date(data) == expected_result


@pytest.mark.unit
@pytest.mark.parametrize(
    'data, expected_result',
    email_examples,
    ids=str,
)
def test_validate_email(data: str, expected_result: bool) -> None:
    assert validate_email(data) == expected_result
