from flask import render_template, request

from dummyData import Jobs_details


def home():
  return render_template('index.html')


def services():
  return render_template('services.html')


def about():
  return render_template('about.html')


def jobs():
  query = request.form.get('query', '')
  if query:
    jobs = [
        job for job in Jobs_details
        if query.lower() in job['title'].lower() or query.lower() in
        job['description'].lower() or query.lower() in job['skills']
        or query.lower() in job['location'].lower() or query.lower() in
        job['experience'].lower() or query.lower() in job['salary'].lower()
    ]
  else:
    jobs = Jobs_details

  return render_template('jobs.html', jobs=jobs)
