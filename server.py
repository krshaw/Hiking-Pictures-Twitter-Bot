from os import environ
from flask import Flask

app = Flask(__name__)

app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Flask server is working</p>'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=33507)

