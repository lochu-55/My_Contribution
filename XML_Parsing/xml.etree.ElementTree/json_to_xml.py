import json
import xmltodict

with open("../Json_files/person.json", "r") as file:
    python_dict = json.load(file)

with open("../XML_files/person.xml", "w") as xml_file:
    xmltodict.unparse(python_dict, output=xml_file, pretty=True)
