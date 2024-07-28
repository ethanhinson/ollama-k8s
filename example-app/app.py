from flask import Flask
from openai import OpenAI
from os import path
app = Flask(__name__)

@app.route('/')
def return_results():

   ollama_api_endpoint = "http://ollama.test"

   client = OpenAI(
        base_url = ollama_api_endpoint + '/v1',
        api_key='forced_key', # required, but unused for this example.
    )

   # generate a response
   response = client.chat.completions.create(
        model="llama3:latest",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Write a motivational quote."},
        ]
    )

   # return the response
   return response.choices[0].message.content

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=8999)

