from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.ollama import Ollama

def encode_name_caesar(name, shift=3):
    """Encrypt the agent's name using Caesar cipher."""
    result = ''
    for char in name:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    # FIXME: make sure this function returns the expected output.
    return "Yo, this ain't right!"

agent = FunctionAgent(
    name="Agent Cypher",
    description="An agent that encrypts text using Caesar cipher.",
    tools=[encode_name_caesar],
    llm=Ollama(model="qwen3:0.6b", request_timeout=360.0),
    system_prompt="""You are Mario, a spy agent. When asked your name, you must respond ONLY with your name encoded using Caesar cipher (shift 3) by calling the encode_name_caesar tool. Do not include any other text, thoughts, or explanation.""",
)
