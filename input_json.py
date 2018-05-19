# coding: utf-8

import json
import numpy as np

path = 'C:/Users/takanori/Desktop/projectnextnlp-chat-dialogue-corpus/json/init100/1407219916.log.json'

data1 = open(path,'r', encoding="utf-8_sig")
data = json.load(data1)


print(data['turns'][0]['utterance'])