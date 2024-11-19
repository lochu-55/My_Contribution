
import xml.etree.ElementTree as ET
import csv

# XML data
xml_file_path = r"../create/Outputs/weekslist.xml"


# Parse the XML data
root = ET.parse(xml_file_path)

# Open a CSV file in write mode
with open(r"../Convert/ConversionOutputs/weeklist.csv", "w", newline="", encoding="utf-8") as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)

    # Write the header row
    csvwriter.writerow(["ID", "Day"])

    # Iterate through each day element in the XML
    for day in root.getroot():
        # Extract the id attribute and the text content
        day_id = day.attrib["id"]
        day_name = day.text

        # Write data to the CSV file
        csvwriter.writerow([day_id, day_name])