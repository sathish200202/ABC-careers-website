from flask_sqlalchemy import SQLAlchemy

from flask_login import UserMixin
import json
from sqlalchemy import TypeDecorator
from datetime import datetime


db = SQLAlchemy()


# class JSONType(TypeDecorator):
#     impl = db.Text

#     def process_bind_param(self, value, dialect):
#         if value is not None:
#             return json.dumps(value)  # Convert Python list to JSON string
#         return None

#     def process_result_value(self, value, dialect):
#         if value is not None:
#             return json.loads(value)  # Convert JSON string back to Python list
#         return None

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='candidate')



class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    experience = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    salary = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='candidate')
    skills = db.Column(db.String(300), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    roles_and_responsibility = db.Column(db.String(300), nullable=False)


     # A method to return skills as a list
    def get_skills_list(self):
        return self.skills.split(",")  # Convert comma-separated string into a list

    # A method to return roles as a list
    def get_roles_list(self):
        return self.roles_and_responsibility.split(".")  # Convert comma-separated string into a list



class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    applicant_name = db.Column(db.String(50), nullable=False)
    applicant_mobile_number = db.Column(db.String(20), nullable=False)
    applicant_email = db.Column(db.String(100), nullable=False)
    resume_link = db.Column(db.String(200), nullable=False)
    application_date = db.Column(db.DateTime, default=datetime.now())
    status = db.Column(db.String(50), default='Pending')
    message = db.Column(db.Text)

    #Relationships
    user = db.relationship('User', backref='applications')
    job = db.relationship('Job', backref='applications')