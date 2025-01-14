import os
from dotenv import load_dotenv
import requests
from flask import Blueprint, request, jsonify

# Load environment variables from .env file
load_dotenv()

class GroupMeBot:
    def __init__(self, convo):
        self.bot_id = os.getenv('GROUPME_BOT_ID')  # Your bot's ID
        self.blueprint = Blueprint('groupme_bot', __name__)
        self._setup_routes()

        # Print a message when the bot is ready
        print(f"✅ GroupMe Bot is ready! Bot ID: {self.bot_id}")

    def _setup_routes(self):
        @self.blueprint.route('/groupme/webhook', methods=['POST'])
        def groupme_webhook():
            data = request.json

            # Log the incoming message
            sender = data.get('name', 'Unknown')
            message = data.get('text', 'No text')
            print(f"📩 Message received from {sender}: {message}")

            # Process user messages (ignore bot messages)
            if 'text' in data and data['sender_type'] != 'bot':
                # Check if the bot is mentioned in the message
                if self.is_mentioned(data):
                    user_message = data['text']
                    response = self.generate_response(user_message)
                    self.send_message(response)

            return jsonify({"status": "ok"})

    def is_mentioned(self, data):
        """
        Check if the message mentions the bot by comparing bot_id in the payload.
        """
        return f"@{self.bot_id}" in data['text']

    def generate_response(self, user_message):
        """
        Logic to generate a bot response.
        """
        return f"Echo: {user_message}"

    def send_message(self, message):
        """
        Sends a message to the GroupMe group via the API.
        """
        url = "https://api.groupme.com/v3/bots/post"
        payload = {
            "bot_id": self.bot_id,
            "text": message
        }
        requests.post(url, json=payload)

def run(self):
    self.bot.run(self.token)
