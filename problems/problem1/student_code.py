import asyncio
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.ollama import Ollama

model: str = "qwen3:0.6b"
my_name: str = "Mario"
shift: int = 3

def encrypt_text(text: str) -> str:
    """Encrypts a text using Caesar cipher. Input is the text to be encrypted."""
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    # FIXME: make sure this function returns the expected output.
    return result

agent = FunctionAgent(
    name="Agent Caesar Cipher",
    description="An agent that knows how to encrypt text using a Caesar cipher.",
    tools=[encrypt_text],
    llm=Ollama(model=model, request_timeout=360.0),
    system_prompt="""You're an helpful AI assistant that can encrypt text.""",
)

async def main():
    response = await agent.run(
        "Encrypt the following text: \"My name is The Llamanator\"."
    )
    print(response)


# Run the agent
if __name__ == "__main__":
    asyncio.run(main())
