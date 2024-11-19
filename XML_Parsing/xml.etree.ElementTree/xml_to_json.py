import json
import xmltodict


with open("../XML_files/sample.xml") as xml_file:
    data_dict = xmltodict.parse(xml_file.read())
    xml_file.close()

    json_data = json.dumps(data_dict, indent=4)

    with open("../Json_files/data.json", "w") as json_file:
        json_file.write(json_data)
        json_file.close()
