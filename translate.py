from matplotlib.pyplot import text
from getting_data import getting_text_data
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-id")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-id")

translator = pipeline("translation", model=model, tokenizer=tokenizer)
text=getting_text_data(1,'data/squad/train-v2.0.json')
print(text)
translated_text=translator(text)
print("\n")
print(translated_text)

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