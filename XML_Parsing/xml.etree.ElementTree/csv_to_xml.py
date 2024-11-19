import pandas as pd
import xml.etree.ElementTree as ET
import xml.dom.minidom


def csv_to_xml(csv_file, xml_file):
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Create root element for XML tree
    root = ET.Element('data')

    # Iterate over rows in DataFrame
    for index, row in df.iterrows():
        # Create child element for each row
        item = ET.SubElement(root, 'item')

        # Add data from DataFrame row as child elements
        for col in df.columns:
            ET.SubElement(item, col).text = str(row[col])

    # Create XML tree
    tree = ET.ElementTree(root)

    # Convert XML tree to string
    xml_string = ET.tostring(root, encoding='unicode')

    # Prettify XML string
    dom = xml.dom.minidom.parseString(xml_string)
    prettified_xml = dom.toprettyxml(indent="  ")

    # Write prettified XML to file
    with open(xml_file, "w") as f:
        f.write(prettified_xml)


# Example usage
csv_to_xml('../CSV_files/email.csv', '../XML_files/email.xml')

