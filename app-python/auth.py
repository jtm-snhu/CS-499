from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from forms import LoginForm, SignupForm
from database import db


auth = Blueprint('auth', __name__)

# Route to login page
@auth.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

# Route to login form submission
@auth.route('/login', methods=['POST'])
def login_post():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        remember = form.remember.data

        user = User.query.filter_by(email=email).first()

        # User must exist and password hash must match
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.', 'danger')
            return redirect(url_for('auth.login'))

        # If we get here, user check passed. Log in.
        login_user(user, remember=remember)
        return redirect(url_for('main.inventory_list'))

    flash('Invalid form submission. Please try again.', 'danger')
    return redirect(url_for('auth.login'))

# Route to signup page
@auth.route('/signup')
def signup():
    form = SignupForm()
    return render_template('signup.html', form=form)

# Signup page form submission
@auth.route('/signup', methods=['POST'])
def signup_post():
    form = SignupForm()
    if form.validate_on_submit():
        email = form.email.data
        name = form.name.data
        password = form.password.data

        # Check to see if user already exists
        if User.query.filter_by(email=email).first():
            flash('That email address already exists.', 'danger')
            return redirect(url_for('auth.signup'))

        # If new user, hash password and add to db
        # Catch database exceptions
        try:
            new_user = User(email=email, name=name, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            flash('Signup successful! Please log in.', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {str(e)}', 'danger')
            return redirect(url_for('auth.signup'))

        # Log new user out so they must sign in to continue
        logout_user()
        return redirect(url_for('auth.login'))

    flash('Invalid form submission. Please try again.', 'danger')
    return redirect(url_for('auth.signup'))

# Route to log user out
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))