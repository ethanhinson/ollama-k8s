import os
from llama_index.core.ingestion import (
    DocstoreStrategy,
    IngestionPipeline,
    IngestionCache,
)
from llama_index.storage.kvstore.redis import RedisKVStore as RedisCache
from llama_index.storage.docstore.redis import RedisDocumentStore
from llama_index.core.node_parser import JSONNodeParser

from model import EmbeddingModel
from vector import Vector

redis_host = os.environ.get("REDIS_HOST", "localhost")
redis_port = os.environ.get("REDIS_PORT", "6379")

class Pipeline:
    def make_pipeline(self):
        embed_model = EmbeddingModel("BAAI/bge-m3").get_model()
        vector_store = Vector().get_store()
        cache = IngestionCache(
            cache=RedisCache.from_host_and_port(redis_host, redis_port),
            collection="redis_cache",
        )
        return IngestionPipeline(
            transformations=[
                JSONNodeParser(),
                embed_model,
            ],
            docstore=RedisDocumentStore.from_host_and_port(redis_host, redis_port, namespace="document_store"),
            vector_store=vector_store,
            cache=cache,
            docstore_strategy=DocstoreStrategy.UPSERTS,
        )