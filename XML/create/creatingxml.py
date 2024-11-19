import xml.etree.ElementTree as ET
import xml.dom.minidom
# Create the root element
root = ET.Element("friendslist")

# Create the friends element
friends = ET.SubElement(root, "friends")

# Create four friend elements with some attributes or text
friend1 = ET.SubElement(friends, "friend")
friend1.set("id", "1")
friend1.text = "Sree jyothsna"

friend2 = ET.SubElement(friends, "friend")
friend2.set("id", "2")
friend2.text = "Deepika"

friend3 = ET.SubElement(friends, "friend")
friend3.set("id", "3")
friend3.text = "Sarika"

friend4 = ET.SubElement(friends, "friend")
friend4.set("id", "4")
friend4.text = "Lucky"

# Create an ElementTree object
tree = ET.ElementTree(root)

# use this to make an indented xml output
xml_str = ET.tostring(root,encoding="utf-8",method="xml")
dom = xml.dom.minidom.parseString(xml_str)
indented = dom.toprettyxml(indent=" ")

with open(r"../create/Outputs/friendslist.xml", "w", encoding="utf-8") as file:
    file.write(indented)

print("Indented XML file created")