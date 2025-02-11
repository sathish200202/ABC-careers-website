from flask import Blueprint, render_template

from services.mainService import home, about, jobs, services
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