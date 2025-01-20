# blueprints/teams.py
# temporary route hack to just make it work
# easier to use if wrapped in a package
import os
from flask import Blueprint, request, Response
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings
from botbuilder.schema import Activity
import logging
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# Load environment variable for GroupMe bot ID
TEAMS_APP_ID = os.getenv("TEAMS_APP_ID")
TEAMS_BOT_ID = os.getenv("TEAMS_BOT_ID")

if TEAMS_APP_ID:
    logger.info("✅ Teams API is ready! App ID: %s", TEAMS_APP_ID)
else:
    logger.error("❌ Teams App ID not found. Check your .env file.")

if TEAMS_BOT_ID:
    logger.info("✅ Teams BOT is ready! Bot ID: %s", TEAMS_BOT_ID)
else:
    logger.error("❌ Teams Bot ID not found. Check your .env file.")

# Define the Blueprint
teams = Blueprint('teams_bot', __name__)

# Initialize the Bot Framework Adapter with your app ID and password
adapter_settings = BotFrameworkAdapterSettings(app_id=TEAMS_APP_ID, app_password=TEAMS_BOT_ID)
adapter = BotFrameworkAdapter(adapter_settings)

@teams.route("/teams/webhook", methods=["POST"])
def messages():
    if request.method == "POST":
        body = request.json
        activity = Activity().deserialize(body)
        auth_header = request.headers.get("Authorization", "")
        response = Response(status=200)
        async def turn_call(turn_context):
            await bot.on_turn(turn_context)
        task = adapter.process_activity(activity, auth_header, turn_call)
        return response
