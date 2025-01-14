from flask import Flask

from flask_cors import CORS
from blueprints import main, api

def create_app():
    """
    Create and configure the Flask app.
    """
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(main)  # No prefix, serves as root route handler

    # Enable CORS for all routes
    CORS(app)

    return app