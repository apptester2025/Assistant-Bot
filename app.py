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
    #https://assistant-bot.onrender.com/groupme_bot/groupme/webhook
    app.register_blueprint(groupme, url_prefix='/groupme_bot')
    #https://assistant-bot.onrender.com/teams_bot/teams/webhook
    app.register_blueprint(teams, url_prefix='/teams_bot')
    app.register_blueprint(main)  # No prefix, serves as root route handler
    #https://32a0-2600-1700-851a-8190-2593-9618-b160-9ef3.ngrok-free.app/teams_bot/teams/webhook
    # Enable CORS for all routes
    CORS(app)

    return app