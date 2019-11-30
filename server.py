from os import environ
from flask import Flask
import bot

app = Flask(__name__)

@app.route('/')
def index():
    if bot.EXECUTING:
        return '<p> twitter bot is running as expected</p>'
    return '<p>Twitter bot is not working</p>'

port = int(environ.get('PORT', 5000))

app.run(host='0.0.0.0', port=port)

