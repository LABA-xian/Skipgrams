# -*- coding: utf-8 -*-
"""
Created on Sun May 13 22:08:10 2018

@author: MB207-1
"""

from nltk import skipgrams
import jieba 
import csv
import re
import gc


f = open('D:/wiki_texts_data.txt','r', encoding='utf-8')


sent = re.sub("[A-Za-z0-9]","",f.read())


    

sent_cut =  jieba.cut(sent)
sent_list = []

for i in sent_cut:
    sent_list.append(i)

j = 0


for i in range(6):
    c = 2
    for k in range(7):
        with open(str(j) + '.csv', 'w', encoding="utf_8_sig", newline='') as csvfile:
            writer = csv.writer(csvfile)
            skipsent = list(skipgrams(sent_list ,c , k))
            writer.writerows(zip(skipsent))
            del skipsent 
            gc.collect()
        j = j + 1
    c = c + 2    