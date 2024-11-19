import xml.etree.ElementTree as ET
mytree = ET.parse("../XML_files/sample.xml")
myroot = mytree.getroot()
print(myroot)
#print(myroot.attrib)

# for child in myroot:
#     for c in child:
#         print("text :",c.text)
#         print("tail :",c.tail)
#         print("atrribute :",c.attrib)
#         print("tag :",c.tag)

for x in myroot.findall('food'):
    item =x.find('item').text
    price = x.find('price').text
    print(item, price)

