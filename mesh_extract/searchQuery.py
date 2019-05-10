#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:46:22 2019

@author: nidhi rastogi
"""
#from file import function

from extractor import returnListMesh,returnDictMesh
from regex import demo
from stopStem import testFuncOld,testFuncNew,tokenize
from nltk.tokenize import word_tokenize


tokenList = dict()
meshTermsInQuery = []
meshDict = dic()
meshDict = ingestor()

def tokenizeQuery(query):
     output = [word_tokenize(i) for i in query]
     return output

def main():
    """ Main program """
    # enter search query string 
    inputString = "Diabetes"
    
    #search tokens in mesh terms
    extractedTokens = tokenizeQuery(inputString)
    
    listMesh = returnListMesh
    dictMesh = returnDictMesh
    maxValuesoFar = 0.0
    matchedMesh = ""
    
    listSimilarityVals = []
    for i in extractedTokens:
        for j in listMesh:
            newVal = demo(i,j)
            if (maxValuesoFar < newVal):
                maxValuesoFar = newVal
                matchedMesh = j
        if matchedMesh in meshDict:
            meshTermsInQuery.append(matchedMesh,meshDict[matchedMesh])    
        
    
    return meshTermsInQuery

    
if __name__ == "__main__":
    main()