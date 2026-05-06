import requests
import json

url = "http://localhost:11434/api/generate"

data = {
    "model": "mistral",
    "prompt": "what is ollama   ",
    "stream": False
}

response = requests.post(url, json=data)

result = response.json()

print(result["response"])