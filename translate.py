import requests
from getting_data import getting_data
API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-id"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

input_query= getting_data()
query_format={"inputs":input_query}
output = query(query_format)