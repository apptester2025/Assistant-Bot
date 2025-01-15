import os
import requests
from flask import Blueprint, request, jsonify
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define the Blueprint
api = Blueprint('api', __name__)

# Load environment variable for GroupMe bot ID
GROUPME_BOT_ID = os.getenv("GROUPME_BOT_ID")

@api.route('/discord-invite', methods=['GET'])
def discord_invite():
    """
    Returns the Discord invite link as a JSON response.
    """
    return jsonify({
        "invite_url": "https://discord.gg/svVAnQ8z"
    })
