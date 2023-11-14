import logging

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from api.forms.services import set_types_for_field, find_matching_template

logger = logging.getLogger(__name__)

router = APIRouter(
    tags=['forms'],
)


@router.post(
    path='/get_form',
    name='Find form',
    description='Find form by data',
)
async def find_form_by_data(data: dict[str, str]) -> JSONResponse:
    sub_data = data

    try:

        if template_name := await find_matching_template(data=sub_data):
            return JSONResponse(
                content={'template_name': template_name},
                status_code=status.HTTP_200_OK,
            )

        logger.debug('Form not found, add types for fields')
        field_types = set_types_for_field(data=sub_data)
        return JSONResponse(
            content=field_types,
            status_code=status.HTTP_201_CREATED,
        )

    except HTTPException as err:
        logger.error(err)
