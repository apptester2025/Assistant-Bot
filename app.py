from flask import Flask

from flask_cors import CORS
from blueprints import main, api, groupme, teams

def create_app():
    """
    Create and configure the Flask app.
    """
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(api, url_prefix='/api')
    #https://fema-compliance-bot.onrender.com/groupme_bot/groupme/webhook
    app.register_blueprint(groupme, url_prefix='/groupme_bot')
    #https://fema-compliance-bot.onrender.com/teams_bot/teams/webhook
    app.register_blueprint(groupme, url_prefix='/teams_bot')
    app.register_blueprint(main)  # No prefix, serves as root route handler

    # Enable CORS for all routes
    CORS(app)

    return app