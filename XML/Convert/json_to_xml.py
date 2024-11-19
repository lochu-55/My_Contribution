import xmltodict
import json

json_file_path = r"../Convert/ConversionOutputs/friendslist.json"

# Open the XML file and read its contents
with open(json_file_path, "r") as json_file:
    json_data = json.load(json_file)


# Print or save the JSON data
print(json_data)

with open(r"../Convert/ConversionOutputs/friendslist.xml","w") as file:
    xmltodict.unparse(json_data,output=file,pretty=True)
