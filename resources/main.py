from flask import Blueprint, render_template, redirect, request, flash, url_for
from .form import OrderForm, ContactForm
from models import Order
from flask_mail import Message, Mail
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

@main.route('/contactform', methods=['POST', 'GET'])
def contactform():
    form = ContactForm(request.form)

    if request.method == 'POST':
        if form.validate() == False:
            flash(f"All fields are required.")
            return render_template('contactform.html', form=form)
        else:
            msg = Message(subject=form.subject.data, sender=form.email.data, recipients=["akorir233@gmail.com"])
            msg.body = "Thanks your message has been recieved. We will get back to you shortly"
            # (form.name.data, form.email.data, form.message.data)
            # mail.send(msg)
            

            return redirect(url_for("main.index"))
    elif request.method == 'GET':
        return render_template("contactform.html", form=form)

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


@main.route('/orders', methods=['GET'])
def orders():
    if request.method == 'GET':
        order = Order.query.all()
    return render_template('order_items.html', order=order)

@main.route('/items')
def status():
    return render_template("status.html")
