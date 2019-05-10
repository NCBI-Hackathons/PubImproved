#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:46:22 2019

@author: nidhi rastogi
"""
#from file import function

import extractor
import regEx
import  stopStem

from nltk.tokenize import word_tokenize


tokenList = dict()
meshTermsInQuery = {}

def testFuncNew(query):
     output = [word_tokenize(i) for i in query]
     return output

def main():
    """ Main program """
    # enter search query string 
    inputString = "bemethyl and isinglass"
    
    #search tokens in mesh terms
    extractedTokens = stopStem.testFuncNew(inputString)
    
    print("************Main program**************")
    print("extractedTokens: ")

    print(extractedTokens)
    
    listMesh = ()
    listMesh = extractor.returnListMesh()#allTokensList
    
    #print(listMesh)
    
    dictMesh = {}
    dictMesh = extractor.returnDictMesh()
    #print(dictMesh)
    
    
    matchedMesh = ""
    maxValuesoFar = 0.0
    
    for i in extractedTokens:
        for j in listMesh:
            newVal = regEx.demo(i,j)
            if (maxValuesoFar < newVal):
                maxValuesoFar = newVal
                matchedMesh = j
        if matchedMesh in dictMesh:
            meshTermsInQuery[matchedMesh] = dictMesh[matchedMesh]    
        print("************meshTermsInQuery***************")
        print(meshTermsInQuery)
    
    return meshTermsInQuery

    
if __name__ == "__main__":
    main()