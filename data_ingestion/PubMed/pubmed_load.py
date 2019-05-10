from rdflib import Graph
import requests
from xml.etree import ElementTree
import urllib
import re
import os
import pandas as pd
import json
import xmltodict

def download_pubmed(disease_term):
    """
    Given a disease term, this function downloads the PMIDs of RCTs related to it.
    We stick to RCTs because these are guaranteed to have MESH terms associated with them.
    Further the data for each of the PMIDs is stored as separate JSON files
    """
    api_key = open("API_Key.keys","r").readline()
    url_address = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=' + disease_term + '+randomized+controlled+trial%5Bpublication+type%5D&retmax=1000&rettype=text'
    print(url_address)
    #url_encodedaddress = urllib.parse.urlencode(url_address)
    r = requests.get(url_address)
    xml_content = ElementTree.fromstring(r.content)
    print(xml_content)
    #Add a pitfall check for empty id nodes
    data_dir = os.makedirs("data/xml/", exist_ok=True)
    ids = [id_node.text for id_node in xml_content.findall('.//Id')]
    already_existingfiles = [re.match(r'(.*).xml', id_present) for id_present in os.listdir("data/xml/")]
    #Ideally when there is an elasticsearch instance running, we would feed the files into that
    for pmid in ids:
        #Only create new files for unseen pmids
        if pmid not in already_existingfiles:
            request_idfetch = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=' + pmid + '&rettype=text&api_key=' + api_key)
            #Fetch content for good requests
            if request_idfetch.status_code == 200:
                xml_contentfetch = ElementTree.fromstring(request_idfetch.content)
                with open("data/xml/" + pmid + ".xml", "w") as f:
                    f.write(ElementTree.tostring(xml_contentfetch).decode("utf-8"))
        else:
            print("ID " + pmid + " already exists not fetching content")
    print(ids)

def convertxml_tojson(data_dir):
    '''
    Given the directory of native XML files, this function converts it to JSON
    '''
    files = [file_name for file_name in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, file_name))]
    count_pmids=0
    for pmid_file in files:
        #Read XML file
        with open(data_dir + pmid_file, 'r') as f:
            xmlString = f.read() 
        #Find the pmid from the file name
        pmid = re.match(r'(.*).xml', pmid_file)[1]    
        #Do a json conversion of the xml string
        jsonString = json.dumps(xmltodict.parse(xmlString))
        os.makedirs("data/json/", exist_ok=True)
        json_filename = 'data/json/' + pmid + '.json'
        with open(json_filename,'w') as f:
            f.write(jsonString)
        count_pmids += 1
    print("Files converted to json : ", count_pmids)


def meshanalysis_ondocument(data_dir):
    '''
    If no mesh terms are associated with a file 
    This function will ideally annotate the document with the MESH on demand API
    '''
    count_nomesh = 0
    files = [file_name for file_name in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, file_name))]
    mesh_countdict = {}
    for pmid_file in files:
        pmid_filecont = ElementTree.parse(data_dir + pmid_file)
        mesh_list = pmid_filecont.findall('.//MeshHeading') 
        if len(mesh_list) == 0:
            count_nomesh += 1
        else:
            #Write frequency to MESH terms file for now
            for mesh_termnode in mesh_list:
                mesh_term = mesh_termnode.find('DescriptorName').text
                if mesh_term not in mesh_countdict.keys():
                    mesh_countdict[mesh_term] = 1
                else:
                    mesh_countdict[mesh_term] += 1
    data = pd.Series(mesh_countdict)
    mydata = data.to_csv('meshcount.csv', sep='|',encoding='utf-8')
    print("Number of files with no associated mesh terms ", count_nomesh)

def extractcontent_fromdocument(data_dir):
    '''
    This function serves to extract the content from the XML:
    In a way that is easily ingestable into elasticsearch
    Here we output a non-nested JSON with a few fields, 
    e.g.: ArticleTitle, AbstractText, AuthorList, PublicationType, MeshHeading 
    '''
    files = [file_name for file_name in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, file_name))]
    simplefields_toinclude = ['PublicationType','Keyword','ArticleTitle']


    for pmid_file in files:
        doc_dict = {}
        pmid = re.match(r'(.*).xml', pmid_file)[1]  
        doc_dict['pmid'] = pmid
        pmid_filecont = ElementTree.parse(data_dir + pmid_file)

        #For fields that are simple lists and have values associated with them        
        for field_s in simplefields_toinclude:
            terms_list = pmid_filecont.findall('.//' + field_s)
            if len(terms_list) > 0:
                if len(terms_list) > 1:
                    doc_dict[field_s] = [t.text for t in terms_list]
                else:
                    doc_dict[field_s] = terms_list[0].text

        #Including a special case for MESHHeadings
        authors_list = pmid_filecont.findall('.//Author')
        if len(authors_list) > 0:
            doc_dict['Authors'] = []
            #Removing none type author issues
            for author_termnode in authors_list:
                full_name = ""
                forename_node = author_termnode.find('ForeName')
                lastname_node = author_termnode.find('LastName')

                if forename_node is not None:
                    full_name += forename_node.text 
                if lastname_node is not None: 
                    full_name += " " + lastname_node.text

                doc_dict['Authors'].append(full_name)
        
        #Including a special case for MESHHeadings
        mesh_list = pmid_filecont.findall('.//MeshHeading')
        if len(mesh_list) > 0:
            doc_dict['MeshHeading'] = [mesh_termnode.find('DescriptorName').text for mesh_termnode in mesh_list]
        else:
            doc_dict['MeshHeading'] = []

        #Extract the portions of abstract
        abstract_comps = pmid_filecont.findall(".//AbstractText")
        if len(abstract_comps) > 0:
            for abstract_comp in abstract_comps:
                #Only allow legit labeled data
                if len(abstract_comp.attrib) > 0:
                    doc_dict['Abstract_' + abstract_comp.attrib['Label']] = abstract_comp.text
        #Creating a dir if it doesn't exist
        os.makedirs("data/json_new/", exist_ok=True)

        with open("data/json_new/" + pmid + ".json", 'w') as outfile:  
            json.dump(doc_dict, outfile, indent=4)
    
    print("Simple non-nested json created")   

if __name__ == '__main__':
    '''
    This entry level function:
    1. download_pubmed: downloads data from Pubmed for a particular term
    2. convertxml_tojson: converts this data dump to json
    3. meshanalysis_ondocument: additionally accumulates MESH terms for all files to build a wordcloud
    '''
    #download_pubmed('diabetes')
    #convertxml_tojson('data/xml/')
    #meshanalysis_ondocument('data/xml/')
    extractcontent_fromdocument('data/xml/')
