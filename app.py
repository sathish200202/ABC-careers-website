from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_login import LoginManager

import os

from models.models import db, User

from routes.mainRoutes import main
from routes.authRoutes import auth
from routes.adminRoutes import admin

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')


db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.loginRoute"


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


app.register_blueprint(main)
app.register_blueprint(auth)
app.register_blueprint(admin)


if __name__ == '__main__':
  # with app.app_context():
  #   db.drop_all()
  #   db.create_all()
  #   print("table created successfully")
  app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT')))
