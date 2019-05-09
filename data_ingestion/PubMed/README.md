# Pre-requisities

## Dowloading the Data

Please download the MeSH dataset from ftp://ftp.nlm.nih.gov/online/mesh/rdf/2019.

The data is in NTriples format.

## Loading the Data in to MongoDB

```
$ mkdir data
$ cp mesh2019.nt data/
```

# Running the Script

```
$ docker build --rm -f "data_ingestion/MeSH/Dockerfile" -t mesh:latest data_ingestion/MeSH
$ docker run mesh:latest
```
