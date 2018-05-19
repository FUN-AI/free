import os

filepath = "E:/AI/venv/chatbot_test/learn_txts"
filename = os.listdir(filepath)
num = 0
for names in filename:
    with open(filepath + "/" + names, 'r', encoding="utf-8_sig") as f:
        datas = f.read()
        print(datas)