import asyncio
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.workflow import step, Event, Workflow, Context, StartEvent, StopEvent
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Configuration
model = "qwen3:0.6b"  # Ollama model for language processing
shift = 3  # Caesar cipher shift value

# Configure global LlamaIndex settings
# - embed_model: HuggingFace embedding model for document vectorization
# - llm: Ollama language model for query processing and agent reasoning
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm = Ollama(model=model, request_timeout=360.0)

# Load documents from the data directory and create a searchable index
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

# Custom Events for Workflow Communication
class QueryStartEvent(StartEvent):
    """Custom StartEvent that carries a query parameter."""
    query: str

class SearchResult(Event):
    """Event to pass search results between workflow steps."""
    result: str


class SearchAgentWorkflow(Workflow):
    """
    Workflow for searching documents and encrypting results.
    
    This workflow implements a two-step process:
    1. Search through briefing documents
    2. Encrypt the answer using Caesar cipher
    """
    
    @step
    async def search_documents_step(self, ev: StartEvent) -> SearchResult:
        """
        Step 1: Search through secret briefing documents.
        
        Args:
            ev: StartEvent containing the query to search for
            
        Returns:
            SearchResult: Event containing the search result
        """
        query = ev.query
        result = await query_engine.aquery(query)
        return SearchResult(result=str(result))

    @step
    async def encrypt_answer_step(self, ev: SearchResult) -> StopEvent:
        """
        Step 2: Encrypt the search result using Caesar cipher.
        
        Args:
            ev: SearchResult event containing the name to encrypt
            
        Returns:
            StopEvent: Final event with encrypted result
        """
        answer = ev.result
        encrypted = ''
        
        # Apply Caesar cipher with the configured shift value
        for char in answer:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                encrypted += chr((ord(char) - base + shift) % 26 + base)
            else:
                encrypted += char
                
        # FIXME: make sure this function returns the expected output.
        # return StopEvent(result="Yo, this ain't right!")
        return StopEvent(result=encrypted)


# Workflow Initialization
search_and_encrypt_workflow = SearchAgentWorkflow()


async def main():
    """
    Main function to execute the search and encrypt workflow.
    
    Runs the workflow with a custom query and prints the encrypted result.
    """
    query = "What is the name of the double agent?"
    result = await search_and_encrypt_workflow.run(query=query)
    print("Encrypted Answer:", result)


if __name__ == "__main__":
    asyncio.run(main())
