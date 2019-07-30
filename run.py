from flask import Flask
from app import db, bcrypt
from flask_login import LoginManager 
from models import User
from meinheld import server
from flask_mail import Message, Mail

mail = Mail()

def create_app(config_filename):
    app = Flask(__name__)
    #db = SQLAlchemy(app)
    db.init_app(app)
    app.config.from_object(config_filename)
    bcrypt.init_app(app)

    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USE_SSL"] = True
    app.config["MAIL_USERNAME"] = "akorir233@gmail.com"
    app.config["MAIL-PASSWORD"] = "Alex1920$$"

    mail.init_app(app)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from resources.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from resources.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    login_manager = LoginManager(app)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get((user_id))
    #from models import db
    #db.init_(app)
    

    return app

if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True, port=5001, threaded=True)