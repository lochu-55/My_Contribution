import xml.etree.ElementTree as ET
import json
import xmltodict

with open(r"../create/Outputs/weekslist.xml") as xml_file:
    dict = xmltodict.parse(xml_file.read())

with open(r"../Convert/ConversionOutputs/weeklist.json","w") as json_file:
    json_data = json.dumps(dict,indent=" ")
    json_file.write(json_data)

print(json_data)