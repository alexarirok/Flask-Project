from flask import Blueprint, render_template, redirect, request, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .form import LoginForm, SignupForm, OrderForm
from models import User, Parcel
from app import db, bcrypt 
from flask_login import current_user, logout_user, login_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        print("error")
        user = User.query.filter_by(email=form.email.data).first() 
        if user:  #and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            print ("Hi")
            return redirect(url_for('main.index'))
        else:
            flash('Login unsuccessfully, Please check your email and password', 'danger')
    return render_template("login.html", title="login", form=form)
     
@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = SignupForm(request.form)
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f"Thanks for singning up {form.email.data}", "success")
        print ("Sucessfully")
        return redirect(url_for('auth.login'))
    return render_template('signup.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
