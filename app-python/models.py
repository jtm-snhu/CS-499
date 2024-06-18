from flask_login import UserMixin
from database import db

'''
Model classes for users and animal types
'''

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(1000), nullable=False)
    def __repr__(self):
        return f'User: {self.name}'

class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal = db.Column(db.String(25), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    acquisition_date = db.Column(db.String(10), nullable=False)
    acquisition_country = db.Column(db.String(100), nullable=False)
    training_status = db.Column(db.String(40), nullable=False)
    reserved = db.Column(db.Boolean, default = False, nullable=False)
    in_service_country = db.Column(db.String(100), nullable=False)
    breed = db.Column(db.String(100), nullable=False)
    
    # Return name and ID if print is requested
    def __repr__(self):
        return f'ID: {self.id} Name:{self.name}'


class Monkey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal = db.Column(db.String(25), nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    acquisition_date = db.Column(db.String(10))
    acquisition_country = db.Column(db.String(100))
    training_status = db.Column(db.String(40))
    reserved = db.Column(db.Boolean)
    in_service_country = db.Column(db.String(100))
    species = db.Column(db.String(50))
    height = db.Column(db.Integer)
    tail_length = db.Column(db.Integer)
    body_length = db.Column(db.Integer)
    
    #Return Name and ID if print is requested
    def __repr__(self):
        return f'ID: {self.id} Name:{self.name}'
    
class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal = db.Column(db.String(25), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    acquisition_date = db.Column(db.DateTime)
    acquisition_country = db.Column(db.String(100))
    training_status = db.Column(db.String(40))
    reserved = db.Column(db.Boolean)
    in_service_country = db.Column(db.String(100))
    breed = db.Column(db.String(100))
    height = db.Column(db.Integer)
    tail_length = db.Column(db.Integer)
    body_length = db.Column(db.Integer)
    
    # Return name and ID is print is requested
    def __repr__(self):
        return f'ID: {self.id} Name:{self.name}'