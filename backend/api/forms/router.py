import logging

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from api.forms.services import get_field_type_priority, find_matching_template

logger = logging.getLogger(__name__)

router = APIRouter(
    tags=['forms'],
)


@router.post(
    path='/get_form',
    name='Find form',
    description='Find form by data',
)
async def find_form_by_data(data: dict) -> JSONResponse:
    try:
        if template_name := await find_matching_template(data=data):
            return JSONResponse(
                content={
                    'template_name': template_name,
                },
            )

        return JSONResponse(
            content=get_field_type_priority(keys=data.keys()),
        )
    except HTTPException as err:
        logger.error(err)
