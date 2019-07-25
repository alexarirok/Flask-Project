from flask import Blueprint, render_template, redirect, request
from werkzeug.security import generate_password_hash, check_password_hash
from .form import LoginForm, SignupForm, OrderForm
from models import User, Parcel


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST', 'GET'])
def login():
    
    form = LoginForm()
    if form.validate_on_submit():
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user, remember=form.remember_me).data()
    return render_template("login.html", title="signin", form=form)
     
@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.email.data, form.password.data)
        db_session.add(user)
        flash('Thanks for signing up')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/placeorder', methods=['POST', 'GET'])
def order():
    form = OrderForm(request.form)
    if request.method == 'POST' and form.validate():
        parcel = Parcel(form.parcel_name.data, form.delivery_destination.data, form.parcel_number.data,
        form.pickup_destinatio.data)
        db_session.add(parcel)
        flash('Parcel order added successfully')
        return redirect(url_for('order'))
    return render_template('order.html', form=form)