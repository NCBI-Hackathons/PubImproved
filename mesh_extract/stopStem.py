#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 21:35:32 2019

@author: nidhi rastogi
"""
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stopwords = stopwords.words('english')

#deprecated
def testFuncOld(text):
    output = ' '.join([word for word in text.split() if word not in stopwords.words("english")])
    return output

def testFuncNew(text):
    stopwords.append(('newWord','and','I','A','And','So','arnt','This','When','It','many','Many','so','cant','Yes','yes','No','no','These','these','also','want','please','show','me'))
    output = ' '.join([word for word in text.split() if word not in stopwords])
    return output

def tokenize(text):
    output = []
    output = [word_tokenize(i) for i in text]
    return output
    
if __name__ == "__main__":
    text = 'bemethyl and isinglass'
    #print(testFuncOld(text))
    #print(testFuncNew(text))
    #print((testFuncNew(text)).split())
