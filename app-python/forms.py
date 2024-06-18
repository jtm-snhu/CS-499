from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField, DateField, BooleanField, PasswordField
from wtforms.validators import Optional, DataRequired, Length, Email, EqualTo

class InventorySearchForm(FlaskForm):
    name = StringField('Name', validators=[Optional()])
    breed = StringField('Breed', validators=[Optional()])
    gender = SelectField('Gender', choices=[('', 'Any'), ('Male', 'Male'), ('Female', 'Female')], validators=[Optional()])
    training_status = SelectField('Training Status', choices=[
        ('', 'Any'), ('Trained', 'Trained'), ('In Progress', 'In Progress'), ('Untrained', 'Untrained')
    ], validators=[Optional()])
    in_service_country = SelectField('In Service Country', choices=[
        ('', 'Any'), ('USA', 'USA'), ('Canada', 'Canada'), ('UK', 'UK')
    ], validators=[Optional()])
    reserved = SelectField('Reserved', choices=[
        ('', 'Any'), ('1', 'Yes'), ('0', 'No')
    ], validators=[Optional()])
    submit = SubmitField('Search')

class AnimalEditForm(FlaskForm):
    animal = StringField('Animal', validators=[DataRequired(), Length(max=25)])
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    gender = StringField('Gender', validators=[Optional(), Length(max=10)])
    age = IntegerField('Age', validators=[Optional()])
    weight = IntegerField('Weight', validators=[Optional()])
    acquisition_date = DateField('Acquisition Date', format='%Y-%m-%d', validators=[Optional()])
    acquisition_country = StringField('Acquisition Country', validators=[Optional(), Length(max=100)])
    training_status = StringField('Training Status', validators=[Optional(), Length(max=40)])
    in_service_country = StringField('In Service Country', validators=[Optional(), Length(max=100)])
    breed = StringField('Breed', validators=[Optional(), Length(max=100)])
    height = IntegerField('Height', validators=[Optional()])
    tail_length = IntegerField('Tail Length', validators=[Optional()])
    body_length = IntegerField('Body Length', validators=[Optional()])
    reserved = SelectField('Reserved', choices=[('1', 'Yes'), ('0', 'No')], validators=[DataRequired()])
    submit = SubmitField('Save')
    delete = SubmitField('Delete')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Your Email"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Your Password"})
    remember = BooleanField('Remember me')
    submit = SubmitField('Login', render_kw={"class": "button is-block is-info is-large is-fullwidth"})

class SignupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Your Email"})
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Your Name"})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)], render_kw={"placeholder": "Your Password"})
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField('Sign Up', render_kw={"class": "button is-block is-info is-large is-fullwidth"})