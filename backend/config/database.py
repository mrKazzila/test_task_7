import json
import logging
from pathlib import Path
from sys import exit
from typing import Any

from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorCursor,
    AsyncIOMotorDatabase,
)

from config.settings import settings

logger = logging.getLogger(__name__)

client: AsyncIOMotorClient = AsyncIOMotorClient(settings().mongo_db.dsn)
db: AsyncIOMotorDatabase = client.get_database(settings().mongo_db.DB_NAME)

collection_cursor: AsyncIOMotorCursor = db.get_collection(
    settings().mongo_db.COLLECTION_NAME,
)


def add_test_templates(
        json_file: Path,
        collection_cursor_: AsyncIOMotorCursor,
) -> None:
    """Add test data from json file to MongoDB collection."""
    try:
        logger.info('Start add test data from file %s', json_file)

        json_data = _get_json_data_from_file(file=json_file)
        [collection_cursor_.insert_one(template) for template in json_data]

        logger.info('Test data successfully added')
    except (FileNotFoundError, Exception) as err:
        logger.error(err)
        exit(err)


def _get_json_data_from_file(file: Path) -> dict[str, Any]:
    """Get data from json file."""
    with open(file, 'r') as json_file:
        return json.load(json_file)
