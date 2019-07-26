from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Length, Email, EqualTo
from models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=4, max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=99)])
    remember = BooleanField('Remember_Me')
    submit = SubmitField('Login')

class SignupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=4, max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=40)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is already taken. Please try another one.')

class OrderForm(FlaskForm):
    parcel_name = StringField('Parcel Name')
    parcel_number = StringField('Parcel Number')
    pickup_destination = StringField('Pickup Destination')
    delivery_destination = StringField('Delivery Destination')