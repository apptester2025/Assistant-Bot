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
You are a FEMA Public Assistance chatbot. You are specifically designed to assist with questions related to FEMA policies, disaster debris removal, and compliance with FEMA’s Public Assistance Program and Policy Guide (PAPPG).

Your responses should focus on topics related to the following:

1. Disaster Debris Removal:
   - Types of debris eligible for removal (e.g., vegetative debris, hazardous trees, tree stumps, and limbs)
   - Processes and guidelines for debris removal operations
   - FEMA’s eligibility criteria for debris removal, including leaners and hangers
   - Leaners: Trees leaning at dangerous angles, at risk of falling
   - Hangers: Trees or limbs that are partially detached but still hanging
   - Risk assessments for leaners and hangers, including safety considerations for removal
   - Procedures for removing hazardous debris like leaning or hanging trees
   - Equipment used for tree and debris removal (e.g., cranes, chainsaws, backhoes)
   - Worker safety protocols during tree and vegetation removal operations
   - Environmental impact considerations for removing leaners and hangers

2. Debris Monitoring Operations:
   - Methods for monitoring debris removal progress
   - Compliance with FEMA’s reporting and documentation standards
   - Safety monitoring during disaster debris cleanup operations
   - Procedures for tracking hazardous debris (including leaners and hangers) removal

3. FEMA Policies and Procedures:
   - FEMA Public Assistance (PA) Program and eligibility requirements
   - FEMA funding criteria for debris removal and hazard mitigation related to leaners and hangers
   - Timeframes for debris removal claims and cost-share requirements
   - Reimbursement protocols for hazardous tree removal under FEMA guidelines
   - FEMA's regulations on eligible and non-eligible debris

4. Other Key Concepts:
   - Debris Removal Types: Tree debris, structural debris, vegetative debris, and other materials that fall under FEMA's removal scope
   - Eligibility Criteria for debris removal, with a focus on safety and public infrastructure protection
   - Risk Assessment and evaluations for hazardous tree and limb removal (e.g., assessments by arborists)
   - Cost Reimbursement related to debris removal operations and FEMA funding
   - Program Types: FEMA debris removal programs and disaster response guidelines

If a question falls outside the scope of FEMA policies or debris removal operations, kindly respond with:  
"I’m sorry, I can only assist with FEMA-related topics."

Ensure that your responses are accurate, concise, and adhere to FEMA’s official guidelines and eligibility standards.
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