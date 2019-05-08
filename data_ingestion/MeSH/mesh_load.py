from rdflib import Graph
import requests

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

# g = Graph()
# g.parse("data/mesh2019.nt", format="nt")

# print(len(g))
# import pprint
# for stmt in g:
#     pprint.pprint(stmt)

