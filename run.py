from flask import Flask
from app import db
from flask_login import LoginManager 

def create_app(config_filename):
    app = Flask(__name__)
    #db = SQLAlchemy(app)
    db.init_app(app)
    app.config.from_object(config_filename)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from resources.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from resources.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    login_manager = LoginManager(app)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    #from models import db
    #db.init_(app)
    

    return app

if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True, port=5001)