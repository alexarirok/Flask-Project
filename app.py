
from flask import Flask, render_template, Blueprint
from flask_restful import Api
from resources.Hello import Hello 

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
api.add_resource(Hello, '/Hello')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/user_change')
def user_change():
    return render_template("user_change.html")

@app.route('/cancelorder')
def cancelorder():
    return render_template("cancelorder.html")

@app.route('/contactform')
def contactform():
    return render_template("contactform.html")

@app.route('/order')
def order():
    return render_template("order.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/status')
def status():
    return render_template("status.html")




if __name__ == "__main__":
    app.run(debug=True)
