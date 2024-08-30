
from server import app  # Import your Flask app instance
from server import init_crowd_density_estimator  # Import the function to initialize your model
from heatmap import map  # Import the map function if needed during startup
from flask_socketio import SocketIO

socketio = SocketIO(app)

def startup():
    init_crowd_density_estimator()

if __name__ == "__main__":
    startup()
    socketio.run(app , debug = True)