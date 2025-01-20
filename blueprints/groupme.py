# blueprints/groupme.py
# temporary route hack to just make it work
# easier to use if wrapped in a package

import os
import requests
import logging
from flask import Blueprint, request, jsonify
from dotenv import load_dotenv
from core import LLMSetup
from expert_instructions import FemaExpert, PAExpert, SOPExpert

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# Define the Blueprint
groupme = Blueprint('groupme_bot', __name__)

# Load environment variable for GroupMe bot ID
GROUPME_BOT_ID = os.getenv("GROUPME_BOT_ID")
if GROUPME_BOT_ID:
    logger.info("✅ GroupMe API is ready! Bot ID: %s", GROUPME_BOT_ID)
else:
    logger.error("❌ GroupMe Bot ID not found. Check your .env file.")

@groupme.route('/groupme/webhook', methods=['POST'])
def groupme_webhook():
    """
    Webhook to receive messages from GroupMe and respond automatically.
    """
    data = request.json

    # Check if the message exists and wasn't sent by a bot
    if 'text' in data and data['sender_type'] != 'bot':
        command_prefix = "/bot"
        message = data['text']
        if message.startswith(command_prefix):
            user_message = message[len(command_prefix):].strip()
            response_message = generate_groupme_response(user_message)
            send_groupme_chunks(response_message)

    return jsonify({"status": "ok"})

def generate_groupme_response(user_message):
    """
    Generate a response to the user message. This is customizable.
    """
    # Select an instruction/name dynamically
    selected_instruction = SOPExpert.instruction
    selected_name = SOPExpert.name
    try:
        llm = LLMSetup("gpt-4o-mini", 0, selected_instruction, selected_name)
        return llm.run(user_message)
    except Exception as e:
        logger.error(f"Error generating response: {e}")
        return "Sorry, I couldn't process your request."

def split_message(response, max_length):
    """
    Splits a long response into smaller chunks respecting the max length.
    Tries to split on word boundaries if possible.
    """
    chunks = []
    while len(response) > max_length:
        # Find the last space within the limit
        split_index = response.rfind(' ', 0, max_length)
        if split_index == -1:
            # If no space is found, split at the max_length
            split_index = max_length
        # Add the chunk and update the response
        chunks.append(response[:split_index])
        response = response[split_index:].lstrip()  # Remove leading spaces
    chunks.append(response)  # Add the last chunk
    return chunks

def send_groupme_chunks(response_message, max_length=1000):
    """
    Sends a long message in chunks via GroupMe webhook.
    """
    chunks = split_message(response_message, max_length)
    for chunk in chunks:
        send_groupme_message(chunk)

def send_groupme_message(message):
    """
    Send a message back to the GroupMe group via the API.
    """
    url = "https://api.groupme.com/v3/bots/post"
    payload = {
        "bot_id": GROUPME_BOT_ID,
        "text": message
    }
    response = requests.post(url, json=payload)
    if response.status_code != 202:
        logger.error(f"Failed to send message: {response.status_code} - {response.text}")
