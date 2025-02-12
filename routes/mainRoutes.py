from flask import Blueprint

from services.mainService import home, about, jobs, services, jobById, jobApply
main = Blueprint('main', __name__)


@main.route('/')
def homeRoute():
  return home()

@main.route('/serivices')
def servicesRoute():
  return services()

@main.route('/about')
def aboutRoute():
  return about()


@main.route('/jobs', methods=['GET', 'POST'])
def jobsRoute():
  return jobs()


@main.route('/job/<int:job_id>')
def getJobRoute(job_id):
  return jobById(job_id)

@main.route('/job/<int:job_id>/apply', methods=['GET', 'POST'])
def jobApplyRoute(job_id):
    return jobApply(job_id)