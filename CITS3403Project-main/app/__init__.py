#from sqlite3.dbapi2 import connect
from flask import Flask
# from datetime import datetime
# import bcrypt
# import sqlite3
import os
from flask_sqlalchemy import SQLAlchemy

file_path = os.path.abspath(os.getcwd())+"/users.db"

app = Flask(__name__)
app.secret_key=os.urandom(24)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_path
db = SQLAlchemy(app)


# from app import models
from app import views
from app import models
