![logo](https://github.com/NCBI-Hackathons/PubMedPlus/blob/master/pubmedplus.png "Logo Title Text 1")
# Broadening the Usability of [Pubmed](https://www.ncbi.nlm.nih.gov/pubmed/)

`### What is Pubmed:` PubMed is a free search engine accessing primarily the MEDLINE database of references and abstracts on life sciences and biomedical topics.

### Motivation

### Goal
Current search capabilities on Pubmed (the latest alpha version)allows for search on Pubmed articles which is based on mesh terms. It’s impractical to assume that non-experts know about the mesh terms or their usage. It does not consider cultural differences in the terms used to describe diseases, conditions, and related information.

For example, search for “Diabetes Melitus” may not be a common practice. But search for Diabetes, Sugar, and so on is more reasonable and expected from a wider audience searching for knowledge sources on pubmed. Specifically, a user may search using not just the term _diabetes_, but also _hypertension_, which may commonly be refered to as high BP. Another use case is that there are instances when search terms can be very restrictive and may not display enough results (this limitations currently exists). A potential way to address this problem is that we can relax search terms and display relevant results related to the scientist.

Therefore, we’re building a **search capability for wider usage** that can perform search on the Pubmed library of articles using commonly used words. 

### We’ve divided our project into multiple phases:

```
1. Given a search query, extract MeSH terms and display relevant publications
2. For restrictive queries that do not yield any or enough results, relax search terms and still display articles that are relevant and related to the User.
3. Enhance search capabilities using commonly used terms
4. Add multiple commonly used terms for search
5. Recommend search terms that can potentially help with a more targeted search
```

### Work Flow Diagram
 
 ![workflow diagram](https://github.com/NCBI-Hackathons/PubMedPlus/blob/master/Workflow_Diagram.png "Logo Title Text 1")


### Steps in Phase I - PubMed Query using Mesh Ontology terms from the User Query

```
1. Download PubMed Dump from [https://www.nlm.nih.gov/databases/download/pubmed_medline.html]
2. Convert the data to JSON format
3. Store the data in MongoDB [https://www.mongodb.com/]
4. Download MeSH Ontology [https://www.nlm.nih.gov/mesh/filelist.html]
5. MeSH terms are queried from the search Query provided by the User
..* These MeSH terms are then used to find all the related articles from the PubMed
```
### Challenges and Learning

`Data challenges`

There are lots of variations in bibliography data, and it is hard to reconcile between different data sources.
Many of the existing eUtils APIs available on NCBI do not interoperate, and do not have easy to parse data formats (e.g. JSON).
There was little documentation for NCBI specific APIs, moreover the documentation was for simpler cases. However, due to the active Slack channel and all the in-house help we received from the hackathon, we were able to refine our API parameters.
Lack of labeled training data for our task of improving Pubmed search.
The latest MeSH vocabulary seem to be only be available in RDF format, and it is not clear if there are datasets in other formats.
Several Heterogeneous data/information sources that are disjoint. This made retrieval of important information slightly difficult


`Software challenges`

Elasticsearch data load issues, due to little or no familiarity with the tool. Additionally, due to the nested nature of our JSON data, we faced issues with loading the data and querying the data comprehensively.
Docker worked well for modularization and containerization. Although, we found it difficult to find a technique to share data between the image and host instance.
Connecting Elasticsearch python wrapper with our flask application
We had issues with exposing our Flask app publicly on AWS.

`Learnings`

Through this hackathon, we were able to learn in a demanding and time-constrained setting. We adopted a problem scoping approach, where we continuously revised our techniques to contribute to our end goal of improving the usability of Pubmed’s search. We faced several challenges along the way some unprecedented, and some expected. Yet through them all, we found workarounds and alternative solutions to showcase our ability to solve a niche problem with improving the flexibility of search. Below are some of our key takeaways and learnings from this event. This hackathon has tested our knowledge of tools, and exposed us to some new and powerful utilities and models.

1. Improved knowledge on Docker and working in a container environment
2. Improved knowledge and experience in developing python Flask applications, and interactive user interface design
3. Increased understanding on elasticsearch, its drawbacks and how it works in various installation environments such as docker, and anaconda virtual environment
4. Deeper understanding of the Mesh Ontology including its structure and hierarchy.
5. Deeper understanding of extracting pertinent information from natural language queries
6. Indepth research and understanding of PubMed, including its API, interface, search functionality and drawbacks

### Steps for Reproducing our work

In our project we have identified different pieces that fit together, but can also be good standalone code and containerized each of the modules  separately. The containerization makes our code reproducible, and also abstracts users from the complexity of the implementation.

Given a query, we tokenize the query and identify MESH terms from it, that are then forwarded to our data store which retrieves documents annotated with these MESH terms. Documentation for each of modules is maintained in separate modules, the links which are below:

1. Pubmed Data Ingestion: [https://github.com/NCBI-Hackathons/PubMedPlus/blob/master/data_ingestion/PubMed/README.md]
2. MESH Data Ingestion: [https://github.com/NCBI-Hackathons/PubMedPlus/blob/master/data_ingestion/MeSH/README.md]
3. Flask Application: [https://github.com/NCBI-Hackathons/PubMedPlus/blob/master/flask_application/README.md]
4. Query tokenisation: [https://github.com/NCBI-Hackathons/PubMedPlus/blob/master/mesh_extract/readme.md]

`Presentation Link :` [https://drive.google.com/file/d/1QWVD2ag2os63QH_mod8MmcaGyX_Rk_I0/view?usp=sharing]

### Contributors

* Shruthi Chari   -  _charis at rpi dot edu_
* Neha Keshan    -  _keshan at rpi dot edu_
* Nkechinyere Agu -  _agun at rpi dot edu_
* Nidhi Rastogi   -  _raston2 at rpi dot edu_
* Oshani W. Seneviratne  - _senevo at rpi dot edu_
