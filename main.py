from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import socketio
from flask_cors import CORS

app = Flask(__name__)
CORS = CORS(app, resources={r"/*": {"origins": "*"}})
socketio_main = SocketIO(app,cors_allowed_origins="*")
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



if __name__ == '__main__':
    socketio_main.run(app, port=5000)
    # socketio_second.wait()
