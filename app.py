
from flask import Flask, render_template, Blueprint
from flask_restful import Api
from resources.Hello import Hello 
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager 
from flask_bcrypt import Bcrypt

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Hello, '/Hello')

app = Flask(__name__)

app.config['SECRET_KEY'] = 'os.urandom(32)'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://alex:postgres@localhost/data"
bcrypt = Bcrypt(app)

db = SQLAlchemy(app)
login_manager = LoginManager(app)

# if __name__ == "__main__":
#     app.run(debug=True)
