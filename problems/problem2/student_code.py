import asyncio
import string

from typing import List, Optional

from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.ollama import Ollama

model: str = "qwen3:0.6b"

def extract_codewords(message: str, codewords: Optional[List[str]] = None) -> List[str]:
    """Find and return a list of code words from the message."""
    if codewords is None:
        codewords = ['eagle', 'package', 'extraction']
    
    # Clean and split the message
    words = message.lower().translate(str.maketrans('', '', string.punctuation)).split()
    found = [word for word in words if word in codewords]
    # FIXME: make sure this function returns the expected output.
    return ["not", "what", "you", "want"]

agent = FunctionAgent(
    name="Agent Code Word Detector",
    description="An agent that scans a message for known code words.",
    tools=[extract_codewords],
    llm=Ollama(model=model, request_timeout=360.0),
    system_prompt="""You're an helpful AI assistant that can extract codewords from text.""",
)

async def main():
    response = await agent.run(
        "The eagle tripped over the package during extraction and blamed the squirrel."
    )
    print(response)


# Run the agent
if __name__ == "__main__":
    asyncio.run(main())