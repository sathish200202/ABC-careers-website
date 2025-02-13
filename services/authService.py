from flask import render_template, request, url_for, redirect
from flask_login import login_user, logout_user

from models.models import db, User
from utils.password_utils import hashing_password, cheching_password
def register():
  if request.method == 'POST':
    fullName = request.form.get('fullName')
    email = request.form.get('email')
    password = request.form.get('password')
    confirmPassword = request.form.get('confirmPassword')
    try:
      if not fullName or not email or not password or not confirmPassword:
        return {'Success': False, 'msg': 'All Feilds are required.'}, 400
      
      if password != confirmPassword:
        return {'Success': False, 'msg': 'The password do not match.'}, 400
    
      existing_user = User.query.filter_by(email=email).first()

      if existing_user:
        return {'Success': False, 'msg': 'This email already exists.'}, 400
      
      hashed_password = hashing_password(password=password)

      new_user = User(fullName=fullName, email=email, password=hashed_password)

      db.session.add(new_user)
      db.session.commit()

      return redirect(url_for('auth.loginRoute'))
    except Exception as e:
      print(f'Error in register {e}')
      return {'Success': False, 'msg': 'Server Error.'}, 500

  return render_template('register.html')



def login():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return {'success': False, 'msg': 'All felds are required.'}, 400

    user = User.query.filter_by(email=email).first()

    try:
      if not user:
        return {'success': False, 'msg': 'Email is invalid.'}, 404
     
      if cheching_password(user.password, password) == False:
       return {'success': False, 'msg': 'Password is invalid.'}, 404
     
      login_user(user)

      if user.role == 'admin':
        return redirect(url_for('admin.adminpanelRoute'))
      return redirect(url_for('main.homeRoute'))

    except Exception as e:
      print(f'Error in login {e}')
      return {'Success': False, 'msg': 'Server Error.'}, 500

  return render_template('login.html')


def logout():
  logout_user()
  return redirect(url_for('main.homeRoute'))