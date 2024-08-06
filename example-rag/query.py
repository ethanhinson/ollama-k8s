from llama_index.core import VectorStoreIndex
from vector import Vector
from model import EmbeddingModel
from llama_index.llms.ollama import Ollama
from llama_index.core import Settings

Settings.llm = Ollama(model="llama3:8b", request_timeout=60.0, base_url="http://ollama.test/v1")

embed_model = EmbeddingModel("BAAI/bge-m3").get_model()
store = Vector().get_store()
index = VectorStoreIndex.from_vector_store(
    store, embed_model
)
query_engine = index.as_query_engine()
response = query_engine.query("What are the most recent OG Jordans?")
print(str(response))