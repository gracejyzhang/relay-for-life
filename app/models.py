from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    admin = db.Column(db.Integer)
    messages = db.relationship('Message', backref='user', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True, unique=True)
    timestamp = db.Column(db.DateTime, index=True)
    location = db.Column(db.String(200), index=True)
    description = db.Column(db.String(500), index=True)

    def __repr__(self):
        return '<Post {}>'.format(self.title)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), index=True, unique=True)
    timestamp = db.Column(db.DateTime, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    

