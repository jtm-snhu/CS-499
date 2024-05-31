from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, inspect
from sqlalchemy_utils import database_exists, create_database

# Initialize database object
db = SQLAlchemy()


def table_exists(db, table_name):
    inspector = inspect(db.engine)
    return inspector.has_table(table_name)