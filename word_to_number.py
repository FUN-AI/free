import numpy as np

class change_word:
    def __init__(self, params):
        self.params = params
        self.e_words = {}
        self.d_words = {}

    def main_change(self, words):
        sentence = {}
        datas = words.split("\n")
        Bname = datas[0][7:10]
        Pname = "海老原"
        P = 0
        B = 0
        for box in range(len(datas)):
            sentence[box] = datas[box].split("\t")
            print(sentence[box])
            if(len(sentence[box])>=3):
                if(sentence[box][1]==Pname):
                    self.e_words[P] = self.e_words[P] + " " + sentence[box][2]
                    P+=1
                    if(sentence[box][1] == sentence[box-1][1]):
                        P-=1
                elif(sentence[box][1]==Bname):
                    self.d_words[B] = self.d_words[B] + ' ' + sentence[box][2]
                    B+=1
                    if (sentence[box][1] == sentence[box - 1][1]):
                        B-=1



        print(sentence)
        return 0, 0

    def change_txt(self, words):
        datas = words.split("\n")