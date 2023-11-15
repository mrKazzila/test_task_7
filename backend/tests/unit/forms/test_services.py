import pytest

from api.forms.services import (
    set_types_for_field,
    _check_form,  # noqa
    _fields_type_match,  # noqa
    _get_data_field_type,  # noqa
)
from tests.unit.forms.parametrize_data import (
    get_data_field_type_example,
    set_types_for_field_example,
)


@pytest.mark.unit
@pytest.mark.parametrize(
    'data, expected_result',
    set_types_for_field_example,
    ids=str
)
def test_set_types_for_field(data, expected_result):
    result = set_types_for_field(data)
    assert result == expected_result


@pytest.mark.unit
def test_check_form(form_template, template_fields, form_data):
    result = _check_form(form_template, template_fields, form_data)
    assert result == form_template['name']


@pytest.mark.unit
def test_fields_type_match(form_template, template_fields, form_data):
    assert _fields_type_match(form_template, template_fields, form_data)


@pytest.mark.unit
@pytest.mark.parametrize(
    'data_field_value, expected_result',
    get_data_field_type_example,
    ids=str,
)
def test_get_data_field_type(data_field_value, expected_result):
    result = _get_data_field_type(data_field_value)
    assert result == expected_result
