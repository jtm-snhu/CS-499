from random import randint
from flask import Flask
from flask_login import LoginManager
from demo_data import create_dogs, create_monkeys

#Database and model declarations separated to avoid
#circular imports with app.py
from database import db, table_exists
from models import User, Animal

#from classes import Dog, Monkey

# Database URI constant for clearer code
db_uri = 'sqlite:///rescue_animals.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

    # Initialize database object
    db.init_app(app)
    
    # Check and create db/tables if needed
    with app.app_context():
        db.create_all()
        db.session.commit()
        print("Tables created.")
    
    # Create animals to populate database if none exist
    with app.app_context():
        animal_exists = Animal.query.first()
        if not animal_exists:
            db.session.add_all(create_dogs(1000))
            db.session.commit()
            db.session.add_all(create_monkeys(1000))
            db.session.commit()

    # Flask login manager to track sessions 
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # Get user by ID field
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # blueprint for search demonstration
    from sort_demo import sort_demo as sort_demo_blueprint
    app.register_blueprint(sort_demo_blueprint)

    return app

def main():
    create_app()


if __name__ == '__main__':
    main()

