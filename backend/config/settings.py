import logging
from functools import lru_cache
from sys import exit
from typing import Annotated

from annotated_types import Ge, Le
from pydantic import ValidationError, MongoDsn
from pydantic_settings import BaseSettings

logger = logging.getLogger(__name__)


class MongoDBSettings(BaseSettings):
    """Settings for MongoDB."""

    MongoDB_VERSION: str

    DB_PROTOCOL: str
    DB_HOST: str
    DB_PORT: Annotated[int, Ge(1), Le(65_535)]
    DB_NAME: str
    COLLECTION_NAME: str = 'forms'

    @property
    def dsn(self) -> MongoDsn:
        url_ = MongoDsn.build(
            scheme=self.DB_PROTOCOL,
            host=self.DB_HOST,
            port=self.DB_PORT,
            path=self.DB_NAME,
        )
        return str(url_)


class Settings(BaseSettings):
    """Main settings for project."""

    mongo_db: MongoDBSettings = MongoDBSettings()

    APP_NAME: str
    APP_HOST: str
    APP_PORT: Annotated[int, Ge(1), Le(65_535)]


@lru_cache
def settings() -> Settings:
    logger.info('Loading settings from env ...')

    try:
        settings_ = Settings()
        return settings_

    except ValidationError as e:
        logger.error(
            'Error at loading settings from env. %(err)s',
            {'err': e},
        )
        exit(e)
