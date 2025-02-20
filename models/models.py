from flask_sqlalchemy import SQLAlchemy

from flask_login import UserMixin
import json
from sqlalchemy import TypeDecorator

db = SQLAlchemy()


class JSONType(TypeDecorator):
    impl = db.Text

    def process_bind_param(self, value, dialect):
        if value is not None:
            return json.dumps(value)  # Convert Python list to JSON string
        return None

    def process_result_value(self, value, dialect):
        if value is not None:
            return json.loads(value)  # Convert JSON string back to Python list
        return None

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='candidate')



class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    experience = db.Column(db.Integer)
    location = db.Column(db.String(150), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    role = db.Column(db.String(50), nullable=False, default='candidate')
    skills = db.Column(JSONType, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    roles_and_responsibility = db.Column(JSONType, nullable=False)


