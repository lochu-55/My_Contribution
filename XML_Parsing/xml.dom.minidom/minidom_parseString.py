from xml.dom import minidom
p1 = minidom.parseString("""<?xml version="1.0"?>
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

print(p1)

tagname = p1.getElementsByTagName("item")
print(tagname[0])

print(tagname[0].attributes["category"].value)

print("number of items in menu :",len(tagname))