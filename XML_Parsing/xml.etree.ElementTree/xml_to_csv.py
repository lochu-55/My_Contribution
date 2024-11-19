# Importing the required libraries
import xml.etree.ElementTree as Xet
import pandas as pd

cols = ["item", "price", "description", "calories"]
rows = []

# Parsing the XML file
xmlparse = Xet.parse('../XML_files/sample.xml')
root = xmlparse.getroot()
for i in root:
    item = i.find("item").text
    price = i.find("price").text
    description = i.find("description").text
    calories = i.find("calories").text

    rows.append({"item": item,
                 "price": price,
                 "description": description,
                 "calories": calories})

df = pd.DataFrame(rows, columns=cols)

# Writing dataframe to csv
df.to_csv('../CSV_files/food.csv')
