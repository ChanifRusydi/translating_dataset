from distutils.file_util import write_file
import json

from matplotlib.font_manager import json_dump
from matplotlib.pyplot import fill

with open('data/squad/train-v2.0.json','r') as f:
    translated_data = json.load(f)

fill_data=translated_data['data'][0]['paragraphs'][0]['context']

# replace_text="""Beyoncé Giselle Knowles-Carter (/bijɒnseɪ/ bee-YON-say) (born September 4, 1981) is an American singer, songwriter, record producer and actress. Born and raised in Houston, Texas, she performed in various singing and dancing competitions as a child, and rose to fame in the late 1990s as lead singer of R&B girl-group Destiny\'s Child. Managed by her father, Mathew Knowles, the group became one of the world\'s best-selling girl groups of all time. Their hiatus saw the release of Beyoncé\'s debut album, Dangerously in Love (2003), which established her as a solo artist worldwide, earned five Grammy Awards and featured the Billboard Hot 100 number-one singles "Crazy in Love" and " Baby Boy" """
# translated_data['data'][0]['paragraphs'][0]['context']=translated_data['data'][0]['paragraphs'][0]['context'].replace(translated_data['data'][0]['paragraphs'][0]['context'],replace_text)
with open('test/train-v2.0.json','w') as f:
    json.dump(fill_data,f)