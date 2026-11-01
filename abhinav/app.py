from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
socketio = SocketIO(app, cors_allowed_origins="*")

# Victim ki website
@app.route('/')
def victim_page():
    return render_template('victim.html')

# Ambulance aur Traffic Control Dashboard
@app.route('/dashboard')
def dashboard_page():
    return render_template('dashboard.html')

# Jab victim SOS button dabayega, ye function chalega
@socketio.on('send_sos')
def handle_sos(data):
    print(f"🚨 EMERGENCY ALERT! Location: {data['lat']}, {data['lng']}")
    # Bina kisi delay ke Ambulance aur Traffic ko data bhej do
    emit('receive_sos', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)