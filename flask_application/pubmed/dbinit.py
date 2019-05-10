import json
import os
import codecs
from pymongo import MongoClient

client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)
db = client.pubmeddb
collection_pubmed = db['pubmed']

def dropPubMed():
    if(collection_pubmed.drop()):
        print("Successfully dropped the pubmed collection")

def loadPubMed():
    print("Loading data in to MongoDB...")
    for filename in os.listdir('data'):
        filenamerp = 'data/'+filename
        if (filename != '.DS_Store'):
            with codecs.open(filenamerp, 'r', encoding='utf-8',
                 errors='ignore') as f:
                file_data = json.load(f)
                collection_pubmed.insert(file_data, check_keys=False)
    # client.close()

def queryAll():
    records = collection_pubmed.find( {} )
    for record in records:
        print(record)

def queryPMId(pmId):
    print("Retrieving the record for "+ str(pmId))
    record = collection_pubmed.find_one({"pmid": "30894898"})
    print(record)
    return record

def queryMeSHTerm(meshTerm):
    print("Retrieving the record for "+ str(meshTerm))
    records = collection_pubmed.find({'MeshHeading': str(meshTerm)})
    for record in records:
        print(record)
    return records

def queryMeSHTerms(meshTerms):
    print("Retrieving the record for meshTerms ")
    records = collection_pubmed.find({'MeshHeading': { "$all": meshTerms } })
    for record in records:
        print(record)
    return records
