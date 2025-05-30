import string
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.ollama import Ollama

# ============================================================
# 🛰️ Challenge 2: Operation Code Word Sweep
# Scan a message for known code words
# ============================================================

def extract_codewords(text, codewords=None):
    """Find and return a list of code words from the message."""
    if codewords is None:
        codewords = ['eagle', 'package', 'extraction']
    
    # Clean and split the text
    words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    found = [word for word in words if word in codewords]
    # FIXME: make sure this function returns the expected output.
    return ["not", "what", "you", "want"]

agent = FunctionAgent(
    name="Agent Code Word Detector",
    description="An agent that scans a message for known code words.",
    tools=[extract_codewords],
    llm=Ollama(model="qwen3:0.6b", request_timeout=360.0),
    system_prompt="""You are a spy agent. For every message, respond ONLY with 
    the output of the extract_codewords tool, and nothing else.""",
)
