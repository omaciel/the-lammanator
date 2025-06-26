import asyncio
from datetime import datetime

from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.ollama import Ollama

model: str = "qwen3:0.6b"

def log_message_to_file(message: str, filename: str = "drop.txt") -> str:
    """Log a message from the LLM to a secure drop file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    
    return filename

agent = FunctionAgent(
    name="Agent Dead Drop Logger",
    description="An agent that logs messages to a secure local file.",
    tools=[log_message_to_file],
    llm=Ollama(model=model, request_timeout=360.0),
    system_prompt="""You're an helpful AI assistant that can save messages 
    to a file.""",
)

async def main():
    response = await agent.run(
        "My name is The Llamanator."
    )
    print(response)


# Run the agent
if __name__ == "__main__":
    asyncio.run(main())
