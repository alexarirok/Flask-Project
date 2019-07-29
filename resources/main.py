from flask import Blueprint, render_template, redirect, request, flash, url_for
from .form import OrderForm
from models import Order
from app import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")


@main.route('/user_change')
def user_change():
    return render_template("user_change.html")

@main.route('/cancelorder')
def cancelorder():
    return render_template("cancelorder.html")

@main.route('/contactform')
def contactform():
    return render_template("contactform.html")

@main.route('/order', methods=['POST', 'GET'])
def order():
    form = OrderForm(request.form)
    if request.method == 'POST':
        parcel_name = request.form.get('parcel_name')
        parcel_number = request.form.get('parcel_number')
        order = Order(parcel_name=form.parcel_name.data, parcel_number=form.parcel_number.data)
        db.session.add(order)
        db.session.commit()
        flash(f"Parcel ordered succesfully")
        return redirect(url_for('main.order'))
    return render_template('order.html', form=form)


@main.route('/status')
def status():
    return render_template("status.html")
