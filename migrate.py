from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from app import db 
from run import create_app
from flask_sqlalchemy import SQLAlchemy


app = create_app('config')

migrate = Migrate(app, db)
manager = Manager(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()