from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
  print('Welcome to the page!')
  return "<h1>Welcome</h1>"


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=int(8080))
