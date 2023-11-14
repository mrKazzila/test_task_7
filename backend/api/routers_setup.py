import logging
from sys import exit

from fastapi import FastAPI

from api.forms.router import router as forms_router
from api.healthcheck.router import router as healthcheck_router

logger = logging.getLogger(__name__)


def routers_setup(app: FastAPI) -> None:
    """Setup project routers."""
    try:
        logger.info('Start routers setup')

        app.include_router(forms_router)
        app.include_router(healthcheck_router)

        logger.info('Routers setup successfully ended')
    except Exception as err:
        logger.error(err)
        exit(err)
