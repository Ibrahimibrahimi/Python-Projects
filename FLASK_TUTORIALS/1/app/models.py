from flask_login import UserMixin
from .extensions import login_manager , db 
from datetime import datetime



class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80),nullable=False)
    password = db.Column(db.String(256), nullable=False)
    bio = db.Column(db.String(300), default="")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    role = db.Column(db.String(20),default="admin")
    def getEmail(self):
        return self.email

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(120), nullable=False)
    text = db.Column(db.String(300), default="")