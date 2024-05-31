from flask import Blueprint, render_template, current_app
from sqlalchemy_utils import database_exists, create_database

main = Blueprint('main', __name__)

@main.route('/')
def index():
    dbase = current_app.config['SQLALCHEMY_DATABASE_URI']
    if not database_exists(dbase):
        create_database(dbase)
        return ('No Database found. Created...')
    else:
        return render_template('index.html')

@main.route('/profile')
def profile():
    return render_template('profile.html')

@main.route('/intake')
def intake():
    return render_template('intake.html')

@main.route('/reserve')
def reserve():
    return render_template('reserve.html')
                           
@main.route('/inventory')
def inventory():
    return render_template('inventory.html')
