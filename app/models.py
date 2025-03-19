from app import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)  
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)  
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), default="user", nullable=False)  

    requests = db.relationship('CashRequest', backref='user', lazy=True)

class CashRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default="pending") 
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)



