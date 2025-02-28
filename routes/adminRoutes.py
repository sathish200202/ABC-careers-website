from flask import Blueprint
from flask_login import login_required
from services.adminServices import (adminpanel, usersDetails, jobsDetails, settings, create_new_job,update_job_details, delete_job_by_id, update_user_by_id, delete_user_by_id, all_job_applications )

admin = Blueprint('admin', __name__)


@admin.route('/admin-panel')
@login_required
def adminpanelRoute():
    return adminpanel()

@admin.route('/users-details', methods=['GET', 'POST'])
@login_required
def usersDetailsRoute():
    return usersDetails()

@admin.route('/jobs-details', methods=['GET', 'POST'])
@login_required
def jobsDetailsRoute():
    return jobsDetails()


@admin.route('/settings', methods=['GET', 'POST'])
@login_required
def settingsRoute():
    return settings()

@admin.route('/create-job', methods=["GET", 'POST'])
@login_required
def create_jobs():
    return create_new_job()

@admin.route('/update-job/<int:job_id>', methods=['GET', 'POS'])
@login_required
def update_job(job_id):
    return update_job_details(job_id)


@admin.route('/job/delete/<int:job_id>', methods=['GET', 'POST'])
@login_required
def delete_job(job_id):
    return delete_job_by_id(job_id)


@admin.route('/user/update/<int:user_id>', methods=['GET', 'POST'])
@login_required
def update_user(user_id):
    return update_user_by_id(user_id)

@admin.route('/user/delete/<int:user_id>', methods=['GET', 'POST'])
@login_required
def delete_user(user_id):
    return delete_user_by_id(user_id)


@admin.route('/job-applications', methods=['GET', 'POST'])
@login_required
def job_applicationsRoute():
    return all_job_applications()