import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = os.urandom(32)
SQLALCHEMY_DATABASE_URI = "postgresql://alex:postgres@localhost/data"