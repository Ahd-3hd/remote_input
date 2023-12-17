from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import socketio

app = Flask(__name__)
socketio_main = SocketIO(app)
# socketio_second = socketio.Client()

# socketio_second.connect('http://127.0.0.1:5001')  # Adjust the URL accordingly



@app.route('/')
def index():
    return render_template('index.html')

@socketio_main.on('keypress')
def handle_keypress(data):
    key = data['key']
    user = data['user']
    
    if user == 'amooda':
        print(f'Key pressed by {user} and emitted: {key}')
        emit('keypress', {'key': key, 'user': user}, broadcast=True)

        # Emit to the second server
        # socketio_second.emit('keypress', {'key': key, 'user': user})


# Your existing Flask-SocketIO code here

if __name__ == '__main__':
    socketio_main.run(app)
    # socketio_second.wait()
