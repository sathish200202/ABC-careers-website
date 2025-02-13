from flask import render_template, url_for, redirect

from models.models import User
from dummyData import Jobs_details
def adminpanel():
    total_users = User.query.count()

    total_jobs = len(Jobs_details)
    print(f"jobs: {total_jobs}")
    return render_template('admin.html', total_users = total_users, total_jobs=total_jobs)



def usersDetails():
    users = User.query.all()
    return render_template('users_details.html', users = users)

def jobsDetails():
    return render_template('jobs_details.html')

def settings():
    return render_template('settings.html')