from xml.dom import minidom
p1 = minidom.parse("../XML_files/sample.xml")

print(p1)

tagname = p1.getElementsByTagName("item")
print(tagname[0])

print(tagname[0].attributes["name"].value)
print(tagname[1].firstChild.data)

for x in tagname:
    print(x.firstChild.data)

print("number of items in menu :",len(tagname))