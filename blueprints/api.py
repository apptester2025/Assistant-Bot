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

@api.route('/groupme/webhook', methods=['POST'])
def groupme_webhook():
    """
    Webhook to receive messages from GroupMe and respond automatically.
    """
    data = request.json

    # Check if the message exists and wasn't sent by a bot
    if 'text' in data and data['sender_type'] != 'bot':
        user_message = data['text']
        response_message = generate_groupme_response(user_message)
        send_groupme_message(response_message)

    return jsonify({"status": "ok"})

def generate_groupme_response(user_message):
    """
    Generate a response to the user message. This is customizable.
    """
    # Example logic: simple echo response
    return f"Echo: {user_message}"

def send_groupme_message(message):
    """
    Send a message back to the GroupMe group via the API.
    """
    url = "https://api.groupme.com/v3/bots/post"
    payload = {
        "bot_id": GROUPME_BOT_ID,
        "text": message
    }
    requests.post(url, json=payload)
