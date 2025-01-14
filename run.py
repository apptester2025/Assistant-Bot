from dotenv import load_dotenv
import os
import threading
from app import create_app
from bots import DiscordBot
from bots import GroupMeBot
from core import LLMSetup
from expert_instructions import FemaExpert

# Load environment variables from .env file
load_dotenv()

# Set open ai key (ugly spot to have this)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set API keys
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Create the Flask app
app = create_app()

# Setup Discord bot with LLM
def start_discord_bot():
    # Select an instruction/name dynamically
    selected_instruction = FemaExpert.instruction
    selected_name = FemaExpert.name

    # Create the LLM and conversation chain
    #gpt-4o-mini
    #gpt-4-turbo
    llm = LLMSetup("gpt-4o-mini",0,selected_instruction,selected_name)
    bot = DiscordBot(llm)
    bot.run()

# Setup Group Me bot with LLM
def start_groupMe_bot():
    # Select an instruction/name dynamically
    selected_instruction = FemaExpert.instruction
    selected_name = FemaExpert.name

    # Create the LLM and conversation chain
    #gpt-4o-mini
    llm = LLMSetup("gpt-4o-mini",0,selected_instruction,selected_name)
    bot = GroupMeBot(llm)
    #bot.run()

if __name__ == '__main__':

    # Start Discord bot in a separate thread
    discord_bot_thread = threading.Thread(target=start_discord_bot)
    discord_bot_thread.start()
    
    # Start GroupMe bot in a separate thread
    groupMe_bot_thread = threading.Thread(target=start_groupMe_bot)
    groupMe_bot_thread.start()

    # Start Flask server
    port = int(os.environ.get("PORT", 4000))
    app.run(host='0.0.0.0', port=port)