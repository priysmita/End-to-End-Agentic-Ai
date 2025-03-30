
from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """
    Basic Chatbot Logic implementation
    """
    def __init__(self, model):
        self.llm = model
        
    def process(self, state: State) -> dict:
        """
        Process input and generate chatbot response
        """
        return {'messages': self.llm.invoke(state['messages'])}