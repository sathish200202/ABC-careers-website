from flask import Blueprint


from services.authService import register, login, logout

auth = Blueprint('auth', __name__)


@auth.route('/register')
def registerRoute():
  return register()

@auth.route('/login')
def loginRoute():
  return login()


@auth.route('/logout')
def logoutRoute():
  return logout()

