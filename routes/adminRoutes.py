from flask import Blueprint
from flask_login import login_required
from services.adminServices import adminpanel, usersDetails, jobsDetails, settings

admin = Blueprint('admin', __name__)


@admin.route('/admin-panel')
@login_required
def adminpanelRoute():
    return adminpanel()

@admin.route('/users-details')
@login_required
def usersDetailsRoute():
    return usersDetails()

@admin.route('/jobs-details')
@login_required
def jobsDetailsRoute():
    return jobsDetails()


@admin.route('/settings')
@login_required
def settingsRoute():
    return settings()

