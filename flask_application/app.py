import os
from pubmed import app
from pubmed import dbinit

if __name__ == "__main__":
    dbinit.dropPubMed()
    dbinit.loadPubMed()
    dbinit.queryAll()
    app.run(host='0.0.0.0', port=5000, debug=True)