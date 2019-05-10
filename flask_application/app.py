import os
from pubmed import app
from pubmed import dbinit

if __name__ == "__main__":
    # Only need to drop for a fresh load
    # dbinit.dropPubMed()
    # dbinit.loadPubMed()
    # dbinit.queryAll()
    dbinit.queryPMId("30894898")
    dbinit.queryMeSHTerm("Aged")
    meshTerms = [
        "Absorptiometry, Photon",
        "Aged",
        "Bone Density",
        "Bone Diseases, Metabolic",
        "Denmark"]
    dbinit.queryMeSHTerm(meshTerms)
    app.run(host='0.0.0.0', port=5000, debug=True)