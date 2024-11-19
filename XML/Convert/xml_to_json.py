import xmltodict
import json

xml_file_path = r"../create/Outputs/friendslist.xml"

# Open the XML file and read its contents
with open(xml_file_path, "r") as xml_file:
    xml_data = xml_file.read()

# Convert XML to dictionary
data_dict = xmltodict.parse(xml_data)

json_data = json.dumps(data_dict, indent=4)

# Print or save the JSON data
print(json_data)

with open(r"../Convert/ConversionOutputs/friendslist.json","w") as file:
    file.write(json_data)
