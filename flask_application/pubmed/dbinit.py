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

    collection_pubmed.insert(file_data)
    # client.close()

def queryAll():
    records = collection_pubmed.find( {} )
    for record in records:
        print(record)

