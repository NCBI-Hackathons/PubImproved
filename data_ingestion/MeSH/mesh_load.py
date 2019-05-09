from rdflib import Graph
import requests
import urllib.parse
from SPARQLWrapper import SPARQLWrapper, JSON

MESH_DOWNLOAD_URL = "ftp://ftp.nlm.nih.gov/online/mesh/rdf/2019/mesh2019.nt.gz"
BLAZEGRAPH_ENDPOINT_URL = "http://192.168.1.128:9999/blazegraph/sparql?query="
OUTPUT_FILENAME = 'output/mesh_labels_notes.csv'

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


synonymQuery = """ select distinct ?term ?label ?note 
{?term <http://id.nlm.nih.gov/mesh/vocab#preferredConcept> ?concept;
rdfs:label ?label;
<http://id.nlm.nih.gov/mesh/vocab#note> ?note;
<http://id.nlm.nih.gov/mesh/vocab#previousIndexing> ?indexing;
<http://id.nlm.nih.gov/mesh/vocab#source> ?source;
}"""

termHierarchyQuery = """
select * 
{?concept <http://id.nlm.nih.gov/mesh/vocab#narrowerConcept> ?narrowerConcept;
          rdfs:label ?label.
 ?narrowerConcept rdfs:label ?narrowerLabel.
} 
LIMIT 100
"""

sparql = SPARQLWrapper("http://192.168.1.128:9999/blazegraph/sparql")
sparql.setQuery(synonymQuery)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

with open(OUTPUT_FILENAME, 'w') as f:
    for result in results["results"]["bindings"]:
        row = str(result["term"]["value"]) + "," + str(result["label"]["value"]) + "," + str(result["note"]["value"])
        f.write("%s\n" % row)