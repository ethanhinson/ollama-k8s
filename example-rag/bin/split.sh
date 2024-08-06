#!/bin/bash
for i in $(seq $(jq '.|length' $(pwd)/example-rag/sample-data/retros.json)); do \
    j=$( expr $i - 1 ); \
    touch $(pwd)/example-rag/db/$j.json; \
    jq ".[$j]" $(pwd)/example-rag/sample-data/retros.json > $(pwd)/example-rag/db/$j.json;  \
done