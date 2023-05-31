from app import db
from datetime import datetime

class Users(db.Model):
    username = db.Column(db.String(length=50), nullable=False, unique=True, primary_key=True)
    email = db.Column(db.String(length=100), unique=True, nullable=False)
    password = db.Column(db.String(length=256), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    games= db.relationship('Progress',backref="made_user",lazy=True)

class Progress(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(length=50), db.ForeignKey('users.username'))
    numFlips=db.Column(db.Integer())

    def __repr__(self):
        return '<Progress  %r>'% self.id
    def __init__(self ,numFlips, username):
        self.numFlips=numFlips
        self.username=username