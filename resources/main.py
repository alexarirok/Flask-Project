from flask import Blueprint, render_template

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

@main.route('/order')
def order():
    return render_template("order.html")


@main.route('/status')
def status():
    return render_template("status.html")
