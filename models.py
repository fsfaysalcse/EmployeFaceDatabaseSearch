# models.py
from app import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    face_encoding = db.Column(db.Text, nullable=False)  # Store serialized face encoding
