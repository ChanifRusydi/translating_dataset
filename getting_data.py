import json
def getting_text_data(index,source_file):
   train_file=open('data/squad/train-v2.0.json','r')
   train_data=json.load(train_file)
   train_file.close()
   text=train_data['data'][index]['paragraphs'][0]['context']
   return text