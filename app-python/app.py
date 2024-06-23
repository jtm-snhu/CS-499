from random import randint
from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from demo_data import create_dogs, create_monkeys

#Database and model declarations separated to avoid
#circular imports with app.py
from database import db
from models import User, Animal

# Database URI constant for clearer code
db_uri = 'sqlite:///rescue_animals.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key-goes-here' # This should be random and not stored in source code
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    csrf = CSRFProtect(app) #Initialize CSRF object to make tokens for form input

    # Initialize database object
    db.init_app(app)
    
    # Check and create db/tables if needed
    # Does nothing if they exist
    with app.app_context():
        db.create_all()
        db.session.commit()
        print("DB check complete")
    
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
    login_manager.login_message_category = "info" #set bulma category of "please log in" message
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # Get user by ID field
        return User.query.get(int(user_id))

    # blueprint for auth routes
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # blueprint for sort comparison demonstration
    from sort_demo import sort_demo as sort_demo_blueprint
    app.register_blueprint(sort_demo_blueprint)

    return app

def main():
    create_app()


if __name__ == '__main__':
    main()

