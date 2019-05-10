# -*- coding: utf-8 -*-
"""
Created on Fri May 10 02:08:00 2019

@author: nnamdy-jnr
"""

from elasticsearch import Elasticsearch
import requests
import json

with open('pubmedTest.json') as f:
    doc = json.load(f)

#
es=Elasticsearch()
#
#e1={
#    "first_name":"nitin",
#    "last_name":"panwar",
#    "age": 27,
#    "about": "Love to play cricket",
#    "interests": ['sports','music'],
#}
#
##print(e1)
#
##Now let's store this document in Elasticsearch 
#res = es.index(index='megacorp',doc_type='employee',id=1,body=e1)

res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
#print(res['result'])

res = es.get(index="test-index", doc_type='tweet', id=1)
#print(res['_source'])

es.indices.refresh(index="test-index")

#res = es.search(index="test-index", body={"query": {"match_all": {}}})
#print("Got %d Hits:" % res['hits']['total'])

res= es.search(index='test-index',body={'query':{'match':{'LastName':'Agrawal'}}})
print(res['hits']['hits'])

#print(res['hits']['hits'])
#for hit in res['hits']['hits']:
#    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])