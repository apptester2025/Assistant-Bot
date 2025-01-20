# blueprints/teams.py
# temporary route hack to just make it work
# easier to use if wrapped in a package
import os
from flask import Blueprint, request, Response
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity
import logging
from dotenv import load_dotenv
from core import LLMSetup
from expert_instructions import SOPExpert
# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# Define the Blueprint
teams = Blueprint('teams_bot', __name__)

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

# Initialize the Bot Framework Adapter with your app ID and password
adapter_settings = BotFrameworkAdapterSettings(app_id=TEAMS_APP_ID, app_password=TEAMS_BOT_ID)
adapter = BotFrameworkAdapter(adapter_settings)

# Define your bot class that will handle the conversation
class TeamsBot:
    async def on_turn(self, turn_context: TurnContext):
        user_input = turn_context.activity.text
        # Select an instruction/name dynamically
        selected_instruction = SOPExpert.instruction
        selected_name = SOPExpert.name
        llm = LLMSetup("gpt-4o-mini", 0, selected_instruction, selected_name)
        # Process the user input through LangChain
        response = llm.run(user_input)
        await turn_context.send_activity(response)

# Initialize your bot instance
bot = TeamsBot()

# Define the webhook route
@teams.route("/teams/webhook", methods=["POST"])
def messages():
    if request.method == "POST":
        # Step 1: Get the incoming request body and the Authorization header
        body = request.json
        auth_header = request.headers.get("Authorization", "")
        
        # Step 2: Check if the Authorization token is valid
        if not auth_header:
            return Response("Unauthorized", status=401)
        
        # Step 3: Create an Activity object from the incoming body
        activity = Activity().deserialize(body)
        
        # Step 4: Define the async turn call for handling bot interaction
        async def turn_call(turn_context: TurnContext):
            await bot.on_turn(turn_context)

        # Step 5: Process the activity using the Bot Framework Adapter
        try:
            # Validate the incoming activity and auth header
            task = adapter.process_activity(activity, auth_header, turn_call)
            task.result()  # Ensure that the task runs to completion
            return Response(status=200)  # Return a success response if everything goes well
        except Exception as e:
            logging.error(f"Error processing activity: {e}")
            return Response("Internal Server Error", status=500)