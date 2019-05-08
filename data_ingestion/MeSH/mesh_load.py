from rdflib import Graph
import requests
from xml.etree import ElementTree


def download_file(url):
    """
    Download the super large file using streaming
    """
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush()
    return local_filename

def download_pubmed(disease_term):
    """
    Given a disease term, this function downloads the PMIDs related to it.
    Further the data for each of the PMIDs is stored as separate JSON files
    """
    r = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=' + disease_term + '&datetype=edat&retmax=100&rettype=text')
    xml_content = ElementTree.fromstring(r.content)
    print(xml_content)
    ids = [id_node.text for id_node in xml_content.findall('.//Id')]
    print(ids)

download_pubmed('diabetes')

# g = Graph()
# g.parse("data/mesh2019.nt", format="nt")

# print(len(g))
# import pprint
# for stmt in g:
#     pprint.pprint(stmt)

