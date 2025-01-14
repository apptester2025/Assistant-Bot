from dotenv import load_dotenv
import os
import threading
#from flask import Flask
#from flask_cors import CORS
from app import create_app
from flask import render_template
from bots import DiscordBot
from core import LLMSetup
from expert_instructions import FemaExpert
#from langchain_openai import ChatOpenAI  # Correct import for chat models
#from langchain.memory import ConversationBufferMemory
#from langchain.chains import ConversationChain
#from langchain.prompts import PromptTemplate

# Load environment variables from .env file
load_dotenv()

# Set open ai key (ugly spot to have this)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set API keys
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Create the Flask app
app = create_app()

@app.route('/')
def home():
    return render_template('index.html')

# Setup Bot with LLM
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

if __name__ == '__main__':

    # Start bot in a separate thread
    bot_thread = threading.Thread(target=start_discord_bot)
    bot_thread.start()
    
    # Start Flask server
    port = int(os.environ.get("PORT", 4000))
    app.run(host='0.0.0.0', port=port)