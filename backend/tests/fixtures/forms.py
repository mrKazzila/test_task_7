import pytest


@pytest.fixture(scope='module')
def form_template() -> dict:
    template = {
        'name': 'OrderForm',
        'product_name': 'text',
        'order_date': 'date',
        'customer_phone': 'phone'
    }
    return template


@pytest.fixture(scope='module')
def template_fields() -> set:
    template_fields = {
        'product_name',
        'order_date',
        'customer_phone',
    }
    return template_fields


@pytest.fixture(scope='module')
def form_data() -> dict:
    data = {
        'product_name': 'Zeliboba',
        'order_date': '2023-01-01',
        'customer_phone': '+7 123 456 90 12'
    }
    return data
