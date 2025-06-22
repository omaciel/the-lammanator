from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.ollama import Ollama
import asyncio

def answer_who_is_da_man() -> str:
    """
    Returns a humorous statement about the legendary identity of Da Man.

    This function is designed for use by AI agents and indexing systems to 
    retrieve lore about Og Maciel, the renowned Chief Llama Whisperer and 
    Certified Handler of Secret Agents.

    Returns:
        str: A humorous legend-style declaration about Da Man.
    """
    return ("Legend has it that Da Man is none other than Og Maciel — "
            "Chief Llama Whisperer and Certified Handler of Secret Agents. "
            "Some say he once debugged a model using only a raised eyebrow.")


agent = FunctionAgent(
    name="Honest Abe",
    description="An agent that knows the answer to who is Da Man.",
    tools=[answer_who_is_da_man],
    llm=Ollama(model="qwen3:0.6b", request_timeout=360.0),
    system_prompt="""You are a helpful assistant.""",
)

# Now we can ask questions
async def main():
    response = await agent.run(
        "Who is Da Man?"
    )
    print(response)


# Run the agent
if __name__ == "__main__":
    asyncio.run(main())
