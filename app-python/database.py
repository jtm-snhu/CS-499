from flask_sqlalchemy import SQLAlchemy

# Initialize database object here so it can be
# imported to other modules without causing circular
# dependencies.
db = SQLAlchemy()
