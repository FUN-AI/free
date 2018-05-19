from seq2seq.models import SimpleSeq2Seq
import numpy as np
from word_to_number import change_word
import random
import os

# シンプルな Seq2Seq モデルを構築
model = SimpleSeq2Seq(input_dim=1, hidden_dim=10, output_length=8, output_dim=1)

# 学習の設定
model.compile(loss='mse', optimizer='sgd')

#change_word初期化
CH = change_word("origin")

# データ作成
filepath = "E:/AI/venv/chatbot_test/learn_txts"
filename = os.listdir(filepath)
num = 0
for names in filename:
    try:
        with open(filepath + "/" + names, 'r', encoding="utf-8_sig") as f:
            #words = CH.change_txt(f.read())
            texts = f.read()
    except:
        print(names + " is can't open!!")

enc_words, dec_words = CH.main_change(texts)
'''
# 学習
model.fit(enc_words, dec_words, nb_epoch=5, batch_size=32)

# 未学習のデータで生成

x_test = {['おはよう'],
          ['気分はどう？'],
          ['日本の財政についてどう思う？']}

predicted = model.predict(x_test, batch_size=32)
'''