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

print(root.tag)
print(root.attrib)

for child in root:
    print(child.tag,child.attrib)