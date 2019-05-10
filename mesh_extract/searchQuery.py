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
    #extractedTokens = set()
    extractedTokens = stopStem.testFuncNew(inputString)
    op = extractedTokens.split()
    
    print("************Main program**************")
    print("extractedTokens: ")

    for i in op:
        print(i)
    
    listMesh = {}
    listMesh = extractor.returnListMesh()#allTokensList
    
    #print(listMesh)
    
    dictMesh = {}
    dictMesh = extractor.returnDictMesh()
    #print(dictMesh)
    
    
    matchedMesh = set()
    maxValuesoFar = 0.0
    strMesh = ""
    
    for i in op:
        #print(i)
        for j in listMesh:
            #print (j)
            newVal = regEx.demo(i,j)
            if (maxValuesoFar < newVal):
                maxValuesoFar = newVal
                strMesh = j
        print ("matchedMesh")
        print (matchedMesh)
        matchedMesh.add(strMesh)
        
        if matchedMesh in dictMesh:
            meshTermsInQuery[matchedMesh] = dictMesh[matchedMesh]    
        print("************meshTermsInQuery***************")
        #print(meshTermsInQuery)
        print(matchedMesh)
    return matchedMesh#meshTermsInQuery

    
if __name__ == "__main__":
    main()