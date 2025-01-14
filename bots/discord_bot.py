import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set up Discord client intents for handling messages
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Required for reading user messages
client = discord.Client(intents=intents)


class DiscordBot:
    def __init__(self, convo):
        # Initialize the bot with command prefix and intents
        self.bot = commands.Bot(command_prefix='!', intents=intents)
        self.token = os.getenv('DISCORD_TOKEN')
        self.convo = convo  # Assign convo instance for chatbot logic

        @self.bot.event
        async def on_ready():
            print(f'✅ {self.bot.user} has connected to Discord!')

        @self.bot.event
        async def on_message(message):
            # Ignore bot's own messages
            if message.author == self.bot.user:
                return

            # Handle user message through convo instance
            user_input = message.content
            response = self.convo.run(user_input)  

            # Split long responses if necessary
            max_message_length = 2000
            if len(response) > max_message_length:
                for i in range(0, len(response), max_message_length):
                    await message.channel.send(response[i:i + max_message_length])
            else:
                await message.channel.send(response)

    def run(self):
        self.bot.run(self.token)