from flask import render_template


def register():
  return render_template('register.html')



def login():
  return render_template('login.html')



def logout():
  return "Logout Succeesfully!"