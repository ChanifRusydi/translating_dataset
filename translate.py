from getting_data import getting_data
from transformers import pipeline
model_checkpoint = "chanifrusydi/marian-finetuned-opus-en-id"
translator = pipeline("translation", model=model_checkpoint)

translated_text=translator(getting_data(1,'data/squad/train-v2.0.json'))


'''Using inference API
import requests
from getting_data import getting_data
API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-id"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

input_query= getting_data()
query_format={"inputs":input_query}
print(query_format)
output = query(query_format)
print(output)
'''