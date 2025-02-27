from flask import render_template, request, redirect, url_for
from flask_login import current_user
import os
from werkzeug.utils import secure_filename

from models.models import db, Job, JobApplication
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
    
  return render_template('jobs.html', jobs=jobs)



def jobById(job_id):
  job = Job.query.filter(Job.id == job_id).first()

  return render_template('job.html', job=job)


def jobApply(job_id):
  #allow file extensions
  ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'txt'}
  UPLOAD_FOLDER = 'uploads/resumes'

  #make the upload folder directory
  if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

  def allowed_file(filename):
      return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
  job = Job.query.get_or_404(job_id)

  if request.method == 'POST':
    applicant_name = request.form.get('fullName')
    applicant_email = request.form.get('email')
    applicant_mobile_number = request.form.get('mobile_number')
    
    message = request.form.get('message')

    if not applicant_name or not applicant_email or not applicant_mobile_number or not message:
      return {'msg': 'All feids are required'}
    
    resume_file = request.files.get('resume_link')
    
    if resume_file:
        filename = secure_filename(resume_file.filename)
        resume_path = os.path.join(UPLOAD_FOLDER, filename)
        resume_file.save(resume_path)

        resume_link = resume_path

    else:
        return {'msg': 'Invalid file type. Please upload a PDF, DOC, DOCX, or TXT file.'}
    
    try:

      new_job_application = JobApplication(user_id=current_user.id, job_id=job.id, applicant_name=applicant_name, applicant_email=applicant_email, applicant_mobile_number=applicant_mobile_number, message=message, resume_link=resume_link)

      db.session.add(new_job_application)
      db.session.commit()
      return redirect(url_for('main.jobsRoute'))
    
    except Exception as e:
      print(f"Error in job application: {e}")
      return redirect(url_for('main.jobsRoute'))

  return render_template('jobApply.html', job = job)
