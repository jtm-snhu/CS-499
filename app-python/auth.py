from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from database import db

auth = Blueprint('auth', __name__)

#Route to login page
@auth.route('/login')
def login():
    return render_template('login.html')

#Route for login form submission (POST)
@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    #User must exist and password hash must match
    #Redirect back to login if either is bad
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    
    #If we get here, user check passed. Log in.
    login_user(user, remember=remember)
    return redirect(url_for('main.inventory_list'))

#Route to signup page
@auth.route('/signup')
def signup():
    return render_template('signup.html')

#Route for signup form submission (POST)
@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    #Check to see if user already exists
    #Return to signup page if true
    user = User.query.filter_by(email=email).first()
    if user:
        flash('That Email address already exists')
        return redirect(url_for('auth.signup'))
    
    #If new user, hash password and add to db
    new_user = User(email=email, name=name, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))