#import xmltodict
#import pprint
#import json

#with open('30851727.xml') as f:
#    doc = xmltodict.parse(f.read())

#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(json.dumps(doc), indent = 2)
#with open('pub_json_converted_output.json', 'w') as out:
 #   json.dump(doc, f, indent = 2)
#    pp.pprint(json.dumps(doc), stream=out)

import json
import xmltodict
 
with open("30851727.xml", 'r') as f:
    xmlString = f.read()
 
#print("XML input (sample.xml):")
#print(xmlString)
     
jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)
 
#print("\nJSON output(output.json):")
#print(jsonString)
 
with open("pub_json_converted_output.json", 'w') as f:
    f.write(jsonString)