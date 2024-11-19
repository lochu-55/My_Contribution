import xml.etree.ElementTree as ET
mytree = ET.parse("../XML_files/sample.xml")
myroot = mytree.getroot()

for description in myroot.iter('description'):
    new_desc = str(description.text) + 'wil be served'
    description.text = str(new_desc)
    description.set('updated', 'yes')

mytree.write('../XML_files/new_line.xml')

ET.SubElement(myroot[0], 'speciality')
for x in myroot.iter('speciality'):
    new_desc = 'South Indian Special'
    x.text = str(new_desc)

mytree.write('../XML_files/new_subElement.xml')

myroot[0][0].attrib.pop('name', None)
mytree.write('../XML_files/pop_nameAttribute.xml')


myroot[0].remove(myroot[0][0])
mytree.write('../XML_files/pop_tag.xml')


myroot[0].clear()
mytree.write('../XML_files/clear_1stSubelement.xml')