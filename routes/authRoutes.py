from flask import Blueprint, render_template
from werkzeug.datastructures import auth

auth = Blueprint('auth', __name__)


@auth.route('/register')
def register():
  return render_template('register.html')


@auth.route('/login')
def login():
  return render_template('login.html')


# @auth.route('/logout')
# def logout():
#   return
