from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    # User model with Flask-Login integration
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    username = db.Column(db.String(20), unique=True, nullable=False)  # Unique username
    password_hash = db.Column(db.String(200), nullable=False)  # Hashed password

    def __init__(self, username, password=None):
        self.username = username
        if password:
            self.set_password(password)  # Hash password on creation

    def set_password(self, password):
        # Hash and store the password
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # Verify password against stored hash
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    # Blog post model
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    title = db.Column(db.String(100), nullable=False)  # Post title
    body = db.Column(db.Text, nullable=False)  # Post content
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Link to user
    user = db.relationship('User', backref='posts')  # Relationship to User, allows user.posts
