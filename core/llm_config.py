from langchain_openai import ChatOpenAI  # Correct import for chat models
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate

def LLMSetup(model: str, temp: float, instruction: str, name: str) -> ConversationChain:
    """
    Initialize and return the conversation chain.

    Args:
        model (str): The LLM model name to use.
        temp (float): The temperature for response variability.
        instruction (str): System instructions for guiding the chatbot's behavior.

    Returns:
        ConversationChain: Configured conversation chain instance.
    """
    # Set up memory and prompt template
    memory = ConversationBufferMemory()
    prompt = PromptTemplate(
        input_variables=["history", "input"],
        template=f"{instruction}\n\n{{history}}\nUser: {{input}}\n{name}:"
    )
    
    # Create and return the conversation chain
    llm = ChatOpenAI(model=model, temperature=temp)
    return ConversationChain(llm=llm, memory=memory, prompt=prompt, verbose=True)
