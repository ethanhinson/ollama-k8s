import os
from redisvl.schema import IndexSchema
from llama_index.vector_stores.redis import RedisVectorStore

class Vector:
    vector_store = None
    def get_store(self):
        if(self.vector_store):
            return self.vector_store
        redis_host = os.environ.get("REDIS_HOST", "localhost")
        redis_port = os.environ.get("REDIS_PORT", "6379")
        custom_schema = IndexSchema.from_dict(
            {
                "index": {"name": "retros", "prefix": "doc"},
                "fields": [
                    {"type": "tag", "name": "id"},
                    {"type": "tag", "name": "doc_id"},
                    {"type": "text", "name": "text"},
                    {
                        "type": "vector",
                        "name": "vector",
                        "attrs": {
                            "dims": 384,
                            "algorithm": "hnsw",
                            "distance_metric": "cosine",
                        },
                    },
                ],
            }
        )

        self.vector_store = RedisVectorStore(
            schema=custom_schema,
            redis_url=print(f"redis://{redis_host}:{redis_port}"),
        )
        return self.vector_store