from rdflib import Graph
import requests
from xml.etree import ElementTree
import urllib
import re
import os

def download_pubmed(disease_term):
    """
    Given a disease term, this function downloads the PMIDs of RCTs related to it.
    We stick to RCTs because these are guaranteed to have MESH terms associated with them.
    Further the data for each of the PMIDs is stored as separate JSON files
    """
    api_key = open("API_Key.keys","r").readline()
    url_address = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=' + disease_term + '+randomized+controlled+trial%5Bpublication+type%5D&retmax=1000&rettype=text'
    print(url_address)
    #url_encodedaddress = urllib.parse.urlencode(url_address)
    r = requests.get(url_address)
    xml_content = ElementTree.fromstring(r.content)
    print(xml_content)
    #Add a pitfall check for empty id nodes
    ids = [id_node.text for id_node in xml_content.findall('.//Id')]
    already_existingfiles = [re.match(r'(.*).xml', id_present) for id_present in os.listdir("data/")]
    #Ideally when there is an elasticsearch instance running, we would feed the files into that
    for pmid in ids:
        #Only create new files for unseen pmids
        if pmid not in already_existingfiles:
            request_idfetch = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=' + pmid + '&rettype=text&api_key=' + api_key)
            #Fetch content for good requests
            if request_idfetch.status_code == 200:
                xml_contentfetch = ElementTree.fromstring(request_idfetch.content)
                with open("data/" + pmid + ".xml", "w") as f:
                    f.write(ElementTree.tostring(xml_contentfetch).decode("utf-8"))
        else:
            print("ID " + pmid + " already exists not fetching content")
    print(ids)

download_pubmed('diabetes')

# g = Graph()
# g.parse("data/mesh2019.nt", format="nt")

# print(len(g))
# import pprint
# for stmt in g:
#     pprint.pprint(stmt)

