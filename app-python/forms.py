from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField, DateField, BooleanField, PasswordField
from wtforms.validators import Optional, DataRequired, Length, Email, EqualTo

# Search form at top of inventory list pages
class InventorySearchForm(FlaskForm):
    name = StringField('Name', validators=[Optional()])
    breed = StringField('Breed', validators=[Optional()])
    gender = SelectField('Gender', choices=[('', 'Any'), ('Male', 'Male'), ('Female', 'Female')], validators=[Optional()])
    training_status = SelectField('Training Status', choices=[('', 'Any'), ('Trained', 'Trained'), ('In Progress', 'In Progress'), ('Untrained', 'Untrained')], validators=[Optional()])
    in_service_country = SelectField('In Service Country', choices=[('', 'Any'), ('USA', 'USA'), ('Canada', 'Canada'), ('UK', 'UK')], validators=[Optional()])
    reserved = SelectField('Reserved', choices=[('', 'Any'), ('1', 'Yes'), ('0', 'No')], validators=[Optional()])
    submit = SubmitField('Search')

# Form to edit/add a single animal
class AnimalEditForm(FlaskForm):
    animal = StringField('Animal', validators=[DataRequired(), Length(max=25)])
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[Optional()])
    age = IntegerField('Age', validators=[Optional()])
    weight = IntegerField('Weight', validators=[Optional()])
    acquisition_date = DateField('Acquisition Date', format='%Y-%m-%d', validators=[DataRequired()])
    acquisition_country = SelectField('Acquisition Country', choices=[('USA', 'USA'), ('UK', 'UK'), ('Canada', 'Canada')], validators=[Optional()])
    training_status = SelectField('Training Status', choices=[('Trained', 'Trained'), ('Untrained', 'Untrained'), ('In Progress', 'In Progress')], validators=[Optional()])
    in_service_country = SelectField('In Service Country', choices=[('USA', 'USA'), ('UK', 'UK'), ('Canada', 'Canada')], validators=[Optional()])
    breed = StringField('Breed', validators=[Optional(), Length(max=100)])
    height = IntegerField('Height', validators=[Optional()])
    tail_length = IntegerField('Tail Length', validators=[Optional()])
    body_length = IntegerField('Body Length', validators=[Optional()])
    reserved = SelectField('Reserved', choices=[('1', 'Yes'), ('0', 'No')], default='0', validators=[Optional()])
    submit = SubmitField('Save')
    delete = SubmitField('Delete')

# User login form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Your Email"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Your Password"})
    remember = BooleanField('Remember me')
    submit = SubmitField('Login', render_kw={"class": "button is-block is-info is-large is-fullwidth"})

# New user signup form
class SignupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Your Email"})
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Your Name"})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)], render_kw={"placeholder": "Your Password"})
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField('Sign Up', render_kw={"class": "button is-block is-info is-large is-fullwidth"})