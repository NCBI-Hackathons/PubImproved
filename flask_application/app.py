import os
from pubmed import app
from pubmed import dbinit

if __name__ == "__main__":
    dbinit.loadPubMedToMongo()
    app.run(host='0.0.0.0', port=5000, debug=True)