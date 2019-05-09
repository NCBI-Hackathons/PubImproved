from rdflib import Graph
import requests
from xml.etree import ElementTree
import urllib

def download_pubmed(disease_term):
    """
    Given a disease term, this function downloads the PMIDs of RCTs related to it.
    We stick to RCTs because these are guaranteed to have MESH terms associated with them.
    Further the data for each of the PMIDs is stored as separate JSON files
    """
    url_address = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=' + disease_term + '+Randomized%20Controlled%20Trial&datetype=edat&retmax=1000&rettype=text'
    print(url_address)
    #url_encodedaddress = urllib.parse.urlencode(url_address)
    r = requests.get(url_address)
    xml_content = ElementTree.fromstring(r.content)
    print(xml_content)
    #Add a pitfall check for empty id nodes
    ids = [id_node.text for id_node in xml_content.findall('.//Id')]

    print(ids)

download_pubmed('diabetes')

# g = Graph()
# g.parse("data/mesh2019.nt", format="nt")

# print(len(g))
# import pprint
# for stmt in g:
#     pprint.pprint(stmt)

