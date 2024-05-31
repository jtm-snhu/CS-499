from random import randint
from flask import Flask

#Database and model declarations separated to avoid
#circular imports with app.py
from database import db, table_exists
from models import User, Dog, Monkey

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
    
    #Create animals to populate database if none exist
    with app.app_context():
        
        dog_exists = Dog.query.first()
        if not dog_exists:
            db.session.add_all(create_dogs())
            db.session.commit()
        
        monkey_exists = Monkey.query.first()
        if not monkey_exists:
            db.session.add_all(create_monkeys())
            db.session.commit()
        

    # blueprint for auth routes in our app
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


def create_dogs():
    # Create list of 1000 dogs for testing
    dogs = []
    print('Creating dogs...')
    for i in range(1000):
        name = f'Dog{i}'
        if i%2 == 0:
            gender = 'male'
        else:
            gender = 'female'
        age = randint(2,20)
        weight = randint(2,50)
        acquisition_date = f'{randint(1,30)}/{randint(1,12)}/{randint(2000, 2024)}'
        acquisition_country = 'United States'
        training_status = 'Complete'
        reserved = False
        in_service_country = 'United States'
        breed = f'Breed{i}'
        # Add entry to list
        dogs.append(Dog(name=name, 
                        gender=gender,
                        age=age,
                        weight=weight,
                        acquisition_date=acquisition_date,
                        acquisition_country=acquisition_country,
                        training_status=training_status,
                        reserved=reserved,
                        in_service_country=in_service_country,
                        breed=breed))
  
    for x in range(10):
        print(dogs[x])

    print(f'Dogs Length: {len(dogs)}')
    return dogs


def create_monkeys():
    # Create list of 1000 monkeys for testing
    monkeys = []
    print('Creating Monkeys...')
    for i in range(1000):
        name = f'Monkey{i}'
        if i%2 == 0:
            gender = 'male'
        else:
            gender = 'female'
        age = randint(2,20)
        weight = randint(2,50)
        acquisition_date = f'{randint(1,30)}/{randint(1,12)}/{randint(2000, 2024)}'
        acquisition_country = 'United States'
        training_status = 'Complete'
        reserved = False
        in_service_country = 'United States'
        species = f'species{i}'
        height = randint(6,28)
        tail_length = randint(2,36)
        body_length = randint(12,24)
        
        # Add entry to list
        monkeys.append(Monkey(name=name,
                              gender=gender,
                              age=age,
                              weight=weight,
                              acquisition_date=acquisition_date,
                              acquisition_country=acquisition_country,
                              training_status=training_status,
                              reserved=reserved,
                              in_service_country=in_service_country,
                              species=species,
                              height=height,
                              tail_length=tail_length,
                              body_length=body_length))
  
    for x in range(10):
        print(monkeys[x])

    print(f'Monkey Length: {len(monkeys)}')
    return monkeys

def main():
    create_app()


if __name__ == '__main__':
    main()

