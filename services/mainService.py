from flask import render_template, request
from flask_login import current_user

from models.models import Job
from dummyData import Jobs_details


def home():
  return render_template('index.html')


def services():
  return render_template('services.html')


def about():
  return render_template('about.html')


def jobs():
  query = request.form.get('query', '')
  if query:
    jobs = [
        job for job in Jobs_details
        if query.lower() in job['title'].lower() or 
        query.lower() in job['description'].lower() or 
        query.lower() in job['skills'] or 
        query.lower() in job['location'].lower() or 
        query.lower() in job['experience'].lower() or 
        query.lower() in job['salary'].lower()
    ]
  else:
    jobs = Job.query.all()
    # for job in jobs:
    #  skill_set = [skill.strip() for skill in job.skills.split(',')]
    # print(f"skill set: {skill_set}")

  return render_template('jobs.html', jobs=jobs)



def jobById(job_id):
  job = next((job for job in Jobs_details if job['id'] == job_id), None)

  return render_template('job.html', job=job)


def jobApply(job_id):
  job = next((job for job in Jobs_details if job['id'] == job_id), None)

  return render_template('jobApply.html', job = job)
