from flask import Blueprint
from flask_login import login_required

from services.authService import register, login, logout

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def registerRoute():
  return register()

@auth.route('/login', methods=['GET', 'POST'])
def loginRoute():
  return login()


@auth.route('/logout')
@login_required
def logoutRoute():
  return logout()

