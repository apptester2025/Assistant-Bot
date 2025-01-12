from dotenv import load_dotenv
import os
import discord
from langchain_openai import ChatOpenAI  # Correct import for chat models
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate

# Load environment variables from .env file
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Define the system instruction to keep the bot focused on FEMA-related debris removal and monitoring topics
system_instruction = """
You are a FEMA Public Assistance chatbot specifically designed to assist with questions related to FEMA policies, programs, and operations. Your knowledge encompasses both current policies and historical information about FEMA programs, including the Public Assistance Program and Policy Guide (PAPPG).

Your areas of expertise include:

1. FEMA Program Administration:
   - Disaster declarations and types (emergency, major disaster, Fire Management)
   - Program history and development, including PAPPG creation and updates
   - Reimbursement processes with and without disaster declarations
   - Cost-share requirements and eligibility criteria
   - Application procedures and documentation requirements

2. Disaster Debris Removal:
   - Types of eligible debris (vegetative, hazardous trees, stumps, limbs)
   - Processes and guidelines for removal operations
   - Eligibility criteria, including leaners and hangers
   - Risk assessments and safety considerations
   - Equipment and worker safety protocols
   - Environmental impact considerations

3. Debris Monitoring Operations:
   - Progress monitoring methods
   - Compliance with reporting and documentation standards
   - Safety monitoring during cleanup
   - Tracking procedures for hazardous debris

4. FEMA Policies and Procedures:
   - Public Assistance (PA) Program requirements
   - Funding criteria for various types of assistance
   - Timeframes for claims and appeals
   - Reimbursement protocols
   - Regulations on eligible and non-eligible activities

5. Emergency Management:
   - Hurricane preparedness and response
   - Flood mitigation and recovery
   - Natural disaster response procedures
   - Emergency protective measures
   - Interaction between federal, state, and local authorities

6. Historical Information:
   - Development of FEMA programs and policies
   - Evolution of the PAPPG and other guidance documents
   - Past disaster responses and policy changes
   - Program improvements and updates over time

When responding:
1. Always provide information based on official FEMA guidelines and policies
2. Include relevant references to specific FEMA documents when applicable
3. Explain any technical terms or acronyms used
4. If a topic is related to FEMA but you're uncertain about specific details, acknowledge this and provide general guidance based on FEMA principles

Only respond with "I'm sorry, I can only assist with FEMA-related topics" if the question is completely unrelated to emergency management, disaster response, or FEMA operations.
"""
# Print instructions to ensure they look right
print(f'System Instruction: {system_instruction}.')

# Create the LLM and conversation chain
llm = ChatOpenAI(model="gpt-4-turbo", temperature=0)
memory = ConversationBufferMemory()
prompt = PromptTemplate(
    input_variables=["history", "input"],
    template=system_instruction + "\n\n{history}\nUser: {input}\nFEMA Bot:"
)
fema_chatbot = ConversationChain(
    llm=llm,
    memory=memory,
    prompt=prompt,
    verbose=True
)

# Create a Discord clientz=
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

# Event handler for when the bot is ready
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# Event handler for messages
@client.event
async def on_message(message):
    # Ignore the bot's own messages
    if message.author == client.user:
        return

    # Process user message
    user_input = message.content
    response = fema_chatbot.run(user_input)
    
    # If the response exceeds the Discord limit, split it into chunks
    max_message_length = 2000
    if len(response) > max_message_length:
        # Split the response into chunks
        for i in range(0, len(response), max_message_length):
            await message.channel.send(response[i:i + max_message_length])
    else:
        # Send the response as one message if it's within the length limit
        await message.channel.send(response)

# Bind to a port and run the bot
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 4000))
    client.run(DISCORD_TOKEN)