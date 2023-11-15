import logging

from motor.motor_asyncio import AsyncIOMotorCursor

from api.forms.validators import (
    validate_date,
    validate_email,
    validate_phone,
)
from config.database import collection_cursor

logger = logging.getLogger(__name__)


async def find_matching_template(data: dict) -> str | None:
    """
    Finds a matching template for the provided data.

    Parameters:

    - data: The data to match against templates.

    Returns: The name of the matching template if found, otherwise None.
    """
    cursor = _get_collection_cursor()
    templates_list: list = await cursor.to_list(length=100)

    for template_ in templates_list:
        template_fields_without_name = set(template_.keys()) - {'_id', 'name'}

        if form_name := _check_form(
                template=template_,
                template_fields=template_fields_without_name,
                data=data,
        ):
            logger.debug('form_name=%s', form_name)
            return form_name

    return None


def set_types_for_field(
        data: dict,
) -> dict[str, str]:
    """
    Analyzes the types of fields in the given data and returns a dictionary
    mapping field names to their inferred types.

    Parameters:

    - data: The input data containing field names and values.

    Returns: A dictionary where keys are field names and values are
    inferred types for each field.
    """
    field_types = {}

    for field_name, field_value in data.items():
        field_types[field_name] = _get_data_field_type(
            data_field_value=field_value,
        )

    return field_types


def _get_collection_cursor() -> AsyncIOMotorCursor:
    """
    Get a cursor for the collection.

    Returns: A cursor for the collection.
    """
    return collection_cursor.find()


def _check_form(
        template: dict,
        template_fields: set,
        data: dict,
) -> str | None:
    """
    Check if the provided data matches the template.

    Parameters:

    - template: The template to match against.
    - template_fields: Set of fields in the template.
    - data: The data to check against the template.

    Returns: The name of the matching template if found.
    """
    is_subset = template_fields.issubset(data.keys())

    if is_subset:
        if _fields_type_match(
                template=template,
                template_fields=template_fields,
                data=data,
        ):
            return template['name']
        logger.debug(
            'Matches between template field name/type and '
            'data name/type not found'
        )

    logger.debug('Subset not found')
    return None


def _fields_type_match(
        template: dict,
        template_fields: set,
        data: dict,
) -> bool:
    """
    Checks if the types of fields in the given data match the types specified
    in the template.

    Parameters:

    - template: The template specifying expected field types.
    - template_fields: A set of field names present in the template.
    - data: The input data to be checked for field type matches.

    Returns: True if all fields have matching types, False otherwise.
    """
    logger.debug('Check fields')

    for field in template_fields:
        template_field_type = template[field]
        data_field_type = _get_data_field_type(
            data_field_value=data[field],
        )

        logger.debug('field=%s', field)
        logger.debug('template_field_type=%s', template_field_type)
        logger.debug('data_field_type=%s', data_field_type)

        if data_field_type != template_field_type:
            return False

    logger.info('All fields types is match!')
    return True


def _get_data_field_type(data_field_value: str) -> str:
    """
    Infers and returns the type of a given data field value based on a set of
    predefined validators.

    Parameters:

    - data_field_value: The value of the data field.

    Returns: The inferred type of the data field
    ('date', 'phone', 'email', or 'text').
    """
    validators = [
        ('date', validate_date),
        ('phone', validate_phone),
        ('email', validate_email),
    ]

    for field_type, validator_func in validators:
        if validator_func(data_field_value):
            return field_type

    return 'text'
