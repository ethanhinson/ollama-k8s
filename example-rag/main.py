import os
import glob
from llama_index.readers.json import JSONReader
from pipeline import Pipeline


loader = JSONReader()

def load_data(path: str):
    d = loader.load_data(input_file=path)
    return d[0]

docs = []
for file in glob.glob("/Users/ethanhinson/dev/ollama-k8s/example-rag/db/*.json"):
    doc = load_data(path=file)
    docs.append(doc)

pipeline = Pipeline().make_pipeline()
pipeline.run(docs)