import xml.etree.ElementTree as ET
import csv

xml_file_path = r"../create/Outputs/friendslist.xml"

# Parse the XML data
root = ET.parse(xml_file_path)

# Open a CSV file in write mode
with open(r"../Convert/ConversionOutputs/friends.csv", "w", newline="", encoding="utf-8") as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)

    # Write the header row
    csvwriter.writerow(["ID", "Name"])

    # Iterate through friend elements
    for friend in root.findall("friends/friend"):
        # Extract data from friend elements
        friend_id = friend.attrib["id"]
        friend_name = friend.text
        # Write data to CSV row
        csvwriter.writerow([friend_id, friend_name])

print("CSV file generated successfully!")


