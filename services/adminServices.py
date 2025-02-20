from flask import render_template, url_for, redirect, request

from models.models import User, Job, db
from dummyData import Jobs_details
def adminpanel():
    total_users = User.query.count()

    total_jobs = len(Jobs_details)
    return render_template('admin.html', total_users = total_users, total_jobs=total_jobs)

def usersDetails():
    users = User.query.all()
    return render_template('users_details.html', users = users)

def jobsDetails():
    jobs = Job.query.all()
    return render_template('jobs_details.html', jobs=jobs)

def settings():
    return render_template('settings.html')

def create_new_job():
    if request.method == 'POST':
        title = request.form.get('title')
        experience = request.form.get('experience')
        location = request.form.get('location')
        salary = request.form.get('salary')
        skills = request.form.get('skills')
        description = request.form.get('description')
        roles_and_responsibility = request.form.get('roles_and_responsibility')

        try:
            new_job = Job(title=title, experience=experience, location=location, salary=salary, skills=skills, description=description, roles_and_responsibility=roles_and_responsibility)

            db.session.add(new_job)
            db.session.commit()

            return redirect(url_for('admin.jobsDetailsRoute'))
        
        except Exception as e:
            print(f"Error in posting new job: {e}")
            return redirect(url_for('admin.jobsDetailsRoute'))

    return render_template('create_jobs.html')


def update_job_details(job_id):
    job = Job.query.filter_by(id=job_id).first()

    if request.method == 'POST':
        title = request.form.get('title')
        experience = request.form.get('experience')
        location = request.form.get('location')
        salary = request.form.get('salary')
        skills = request.form.get('skills')
        description = request.form.get('description')
        roles_and_responsibility = request.form.get('roles_and_responsibility')
    

        try:
            job.title = title
            job.experience = experience
            job.location = location
            job.salary = salary
            job.skills = skills
            job.description = description
            job.roles_and_responsibility = roles_and_responsibility

            db.session.commit()
            return redirect(url_for('admin.jobsDetailsRoute'))
        except Exception as e:
            print(f"Error in deleting job: {e}")
            return redirect(url_for('admin.jobsDetailsRoute'))
    return render_template('update_job.html', job=job)
def delete_job_by_id(job_id):
    job = Job.query.filter_by(id=job_id).first()
    try:
        db.session.delete(job)
        db.session.commit()
        return redirect(url_for('admin.jobsDetailsRoute'))
    except Exception as e:
        print(f"Error in deleting job: {e}")
        return redirect(url_for('admin.jobsDetailsRoute'))
    