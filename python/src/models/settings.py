from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

import os

import pymysql
pymysql.install_as_MySQLdb()

DATABASE_CONFIG = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    os.environ.get('DB_USER'),
    os.environ.get('DB_PASS'),
    os.environ.get('DB_HOST'),
    os.environ.get('DB_NAME')
)

DATABASE_ENGINE = create_engine(
    DATABASE_CONFIG,
    encoding='utf-8',
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = DATABASE_ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()
