from doctest import Example
import json
def getting_data():
   train_file=open('data/squad/train-v2.0.json','r')
   train_data=json.load(train_file)
   train_file.close()
   
   print((train_data['data'][0]['paragraphs'][0]['qas'][0]['answers'][0]['text']))
   print((train_data['data'][0]['paragraphs'][0]['qas'][0]['question']))

getting_data()