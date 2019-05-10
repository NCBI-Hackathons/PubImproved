# Pre-requisities

Create an API key by following instructions from this link: https://ncbiinsights.ncbi.nlm.nih.gov/2017/11/02/new-api-keys-for-the-e-utilities/. This key is necessary for programmatically downloading articles from Pubmed.

Store this API key in the API_Key.keys

# Running the Script

```
$ docker build --rm -f "Dockerfile" -t pubmed:latest .
$ docker run pubmed:latest
```
