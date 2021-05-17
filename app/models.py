from app import db
from datetime import datetime

class Users(db.Model):
    username = db.Column(db.String(length=50), nullable=False, unique=True, primary_key=True)
    email = db.Column(db.String(length=100), unique=True, nullable=False)
    password = db.Column(db.String(length=256), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Users {}>'.format(self.username)
