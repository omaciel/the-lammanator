from datetime import datetime

from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.ollama import Ollama

# ============================================================
# 🗃️ Challenge 3: Operation Dead Drop Logger
# Log messages (e.g., from an LLM) to a secure local file
# ============================================================

def log_message_to_file(message, filename="drop.txt"):
    """Log a message from the LLM to a secure drop file."""
    # FIXME: make sure this function returns the expected output.
    message = "Yo, this ain't right!"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    return filename

agent = FunctionAgent(
    name="Agent Dead Drop Logger",
    description="An agent that logs messages to a secure local file.",
    tools=[log_message_to_file],
    llm=Ollama(model="qwen3:0.6b", request_timeout=360.0),
    system_prompt="""You are a spy agent. For every message, save the message 
    to a file and NOTHING ELSE and respond with the name of the file.""",
)
