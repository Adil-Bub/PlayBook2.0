from flask import Flask, render_template
from flask_socketio import SocketIO, send
import time
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('message')
def message(data):
    timestamp = time.strftime('%I:%M %p', time.localtime())
    send([timestamp] + data)


if __name__ == '__main__':
    app.run()
