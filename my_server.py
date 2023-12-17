from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from pynput.keyboard import Key, Controller
from flask_cors import CORS


keyboard = Controller()


app = Flask(__name__)
CORS = CORS(app, resources={r"/*": {"origins": "*"}})

socketio = SocketIO(app,cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('receive_press')
def handle_keypress(data):
    key = data['key']
    user = data['user']
    
    print(f'Key pressed by {user} on server2: {key}')
    keyboard.press(key)
if __name__ == '__main__':
    socketio.run(app, port=5001)
