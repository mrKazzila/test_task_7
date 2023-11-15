import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI

from api.routers_setup import routers_setup
from config.database import add_test_templates, collection_cursor

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app_: FastAPI):
    logger.info('Service started')

    add_test_templates(
        json_file=Path(Path(__file__).parent / 'list_templates_form.json').resolve(),
        collection_cursor_=collection_cursor,
    )

    yield

    logger.info('Service exited')


app = FastAPI(
    title='Test task',
    description=(
        'Create by '
        '<a href="mailto:kazzilacareer@gmail.com?'
        'subject=[TestTask]%20🔥%20Feedback&'
        'body=Hi%20Ilya%2C%0A%0AI%27m%20coming%20to%20you%20today%20'
        'after%20seeing%20your%20solution%20'
        'of%20the%20test%20task%20for%20...">'
        'kazzilacareer@gmail.com'
        '</a>'
    ),
    lifespan=lifespan,
)

routers_setup(app=app)
