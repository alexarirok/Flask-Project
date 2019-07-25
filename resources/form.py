from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired])
    password = PasswordField('Password', validators=[DataRequired])
    remember_me = BooleanField('Remember_Me')
    submit = SubmitField('Signin')

class SignupForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired])
    password = PasswordField('New Password', validators=[DataRequired])
    confirm = PasswordField('Repeat Password')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class OrderForm(FlaskForm):
    parcel_name = StringField('Parcel Name')
    parcel_number = StringField('Parcel Number')
    pickup_destination = StringField('Pickup Destination')
    delivery_destination = StringField('Delivery Destination')