from flask import Flask
from flask_cors import CORS
from config import Config
from logger import setup_logging

# Initialize the Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Enable CORS for all routes
CORS(app)

# Setup logging
setup_logging()

@app.route('/')
def home():
    return "Welcome to MultiMediSync-Core API!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
