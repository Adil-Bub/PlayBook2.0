from flask import Flask, render_template
from flask_socketio import SocketIO, send
from datetime import timedelta, datetime
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('message')
def message(data):
    time = datetime.now()+timedelta(hours=5,minutes=30)
    h = '0'+str(time.hour) if time.hour <= 9 else str(time.hour) 
    m = '0'+str(time.minute) if time.minute <= 9 else str(time.minute) 
    s = '0'+str(time.second) if time.second <= 9 else str(time.second) 
    timestamp = f'{h}:{m}:{s}'
    send([timestamp] + data, broadcast=True)


if __name__ == '__main__':
    app.run()
