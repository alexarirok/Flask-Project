import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'helloworld'
SQLALCHEMY_DATABASE_URI = "postgresql://alex:postgres@localhost/store"