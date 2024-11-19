import xml.etree.ElementTree as ET
import xml.dom.minidom

root = ET.Element("Weeklist")

Day1 = ET.SubElement(root,"Day1")
Day1.set("id","1")
Day1.text = "Sunday"

Day2 = ET.SubElement(root,"Day2")
Day2.set("id","2")
Day2.text = "Monday"

Day3 = ET.SubElement(root,"Day3")
Day3.set("id","3")
Day3.text = "Tuesday"

Day4 = ET.SubElement(root,"Day4")
Day4.set("id","4")
Day4.text = "Wednesday"

Day5 = ET.SubElement(root,"Day5")
Day5.set("id","5")
Day5.text = "Thursday"

Day6 = ET.SubElement(root,"Day6")
Day6.set("id","6")
Day6.text = "Friday"

Day7 = ET.SubElement(root,"Day7")
Day7.set("id","7")
Day7.text = "Saturday"

xml_str = ET.tostring(root,encoding="utf-8",method="xml")

dom = xml.dom.minidom.parseString(xml_str)

indented = dom.toprettyxml(indent=" ")

with open(r"../create/Outputs/weekslist.xml", "w") as file:
    file.write(indented)