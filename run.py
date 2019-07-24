from flask import Flask

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from resources.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from resources.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    #from models import db
    #db.init_(app)
    
    return app

if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)