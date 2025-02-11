class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  fullName = db.Column(db.String(200), nullable=False)
  email = db.Column(db.String(100), nullable=False)
  password = db.Column(db.String(200), nullable=False)


class Job(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(200), nullable=False)
  description = db.Column(db.String(200), nullable=False)
  employer = db.Column(db.String(200), nullable=False)
  location = db.Column(db.String(200), nullable=False)
  salary = db.Column(db.String(200), nullable=False)
  date = db.Column(db.String(200), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  user = db.relationship('User', backref=db.backref('jobs', lazy=True))
