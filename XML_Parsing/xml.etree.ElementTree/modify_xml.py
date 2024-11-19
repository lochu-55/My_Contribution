import xml.etree.ElementTree
from xml.etree import ElementTree as et

root = et.fromstring("""<?xml version="1.0"?>
<store>
    <item category="weapon">
        <power>50</power>
        <cost>30</cost>
    </item>
    <item category="spell">
        <power>80</power>
        <cost>100</cost>
    </item>
</store>
 """)


root.tag = "shop"
print(root.tag)

new_ele = xml.etree.ElementTree.SubElement(root,"item")
new_ele.attrib = {"category":"shield"}

for child in root:
    print(child.tag,child.attrib)

print("after removing newly added sub element")
root.remove(new_ele)
for child in root:
    print(child.tag,child.attrib)