import os
from re import TEMPLATE
from xmlrpc.client import SERVER_ERROR


DEBUG = True


USERNAME = 'postgres'
PASSWORD = '1207'
HOST = 'localhost'
DB = 'boreal'

TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# SQLALCHEMY_DATABASE_URI = f'sqlite:///refractive.sqlite3'
SQLALCHEMY_DATABASE_URI = f'postgresql://{USERNAME}:{PASSWORD}@{HOST}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "4F76CC33D7F321B21A7715EDD5F6FF2075A2ED44E72D295544FBB288079542F5"

BABEL_DEFAULT_LOCALE = 'pt-br'
