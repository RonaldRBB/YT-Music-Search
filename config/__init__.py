"""Configuracion."""
from decouple import config
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm.session import sessionmaker

# APP
# -----------------------------------------------------------------------------
APP_HOST = config("APP_HOST")
APP_PORT = config("APP_PORT")
APP_DEBUG = config("APP_DEBUG")
DOWNLOAD_PATH = config("DOWNLOAD_PATH")
FILES_PATH = config("FILES_PATH")
# DB
# -----------------------------------------------------------------------------
DB_CONNECTION = config("DB_CONNECTION")
DB_HOST = config("DB_HOST")
DB_PORT = config("DB_PORT")
DB_DATABASE = config("DB_DATABASE")
DB_USERNAME = config("DB_USERNAME")
DB_PASSWORD = config("DB_PASSWORD")
DB_PREFIX = config("DB_PREFIX")
# ORM
Base = declarative_base()
engine: Engine = create_engine(
    f"{DB_CONNECTION}://"
    f"{DB_USERNAME}:"
    f"{DB_PASSWORD}@"
    f"{DB_HOST}/"
    f"{DB_DATABASE}", echo=False)
print("-" * 100)
session = sessionmaker(engine)()
