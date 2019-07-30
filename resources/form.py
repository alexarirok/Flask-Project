from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextField
from wtforms.validators import DataRequired, ValidationError, Length, Email, EqualTo
from models import User, Order

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=4, max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4)])
    remember = BooleanField('Remember_Me')
    submit = SubmitField('Login')

class SignupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=4, max=40)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is already taken. Please try another one.')

class OrderForm(FlaskForm):
    parcel_name = StringField('Parcel_Name', validators=[DataRequired(), Length(min=2, max=255)])
    parcel_number = StringField('Parcel_Number', validators=[DataRequired(), Length(min=4)])
   

    submit = SubmitField('Place Order')

    # def validate_parcel(self, order):
    #     order = Order.query.filter_by(parcel=parcel.data).first()

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=2, max=100)])
    subject = TextField('Subject', validators=[DataRequired])
    message = TextField('Message', validators=[DataRequired])
    submit = SubmitField('Send')

    
       