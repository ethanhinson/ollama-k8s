# Minimal example of running LLama with Kubernetes

Uses the `ollama/ollama` image from Docker Hub.

## Prerequisites

- Running Kubernetes cluster
- `kubectl` installed and configured
- `helm` installed
- `ingress-nginx` installed in the cluster
- A local container registry running at `http://localhost:5000`
- Python 3.8 or later

You can find an example using `kind` here: [Kubernetes and You](https://github.com/ethanhinson/kubernetes-and-you)

## Execute the demo

- Apply the helm chart

```bash
helm upgrade --install ollama ./ollama -f ./ollama/values.yaml -n ollama
```

- Execute the example Python script to start a Flask server

```bash
pip install -r example-app/requirements.txt
python ./example-app/app.py
```

- Visit `http://localhost:8999` in your browser to receive a motivational llama message.

## RAG Pipeline

An example real time RAG pipeline is provided. We use Redis as a vector database and document cache.

### Pre-requisites

Assuming you have the provided `kind` cluster running locally. You can use the following to install a redis Helm chart:

`helm -n redis  install redis oci://registry-1.docker.io/bitnamicharts/redis --create-namespace`