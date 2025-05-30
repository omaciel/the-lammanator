from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import asyncio
import os

# Settings control global defaults
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm = Ollama(model="qwen3:0.6b", request_timeout=360.0)

# Create a RAG tool using LlamaIndex
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(
    documents,
    # we can optionally override the embed_model here
    # embed_model=Settings.embed_model,
)
query_engine = index.as_query_engine(
    # we can optionally override the llm here
    # llm=Settings.llm,
)


def encode_name_cypher(name: str, shift=3) -> str:
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

async def search_documents(query: str) -> str:
    """Used to read the secret briefing document."""
    response = await query_engine.aquery(query)
    return str(response)


# Create an enhanced workflow with both tools
agent = AgentWorkflow.from_tools_or_functions(
    [search_documents, encode_name_cypher],
    llm=Settings.llm,
    system_prompt="""You are a helpful assistant that can perform calculations
    and search through documents to answer questions in encoded cypher.""",
)


# Now we can ask questions about the documents or do calculations
async def main():
    response = await agent.run(
        "Look at the briefing named The Lammanator Files and tell me what it is about."
    )
    print(response)


# Run the agent
if __name__ == "__main__":
    asyncio.run(main())