<<<<<<< HEAD
import json
import csv

# Simple nested JSON object to csv converter
# Steps to use
# Step 1 - Change input_file to file that contains json data
# Step 2 - Change output_file to name of wanted output file
# Step 3 - Add more desired fieldnames as needed, this simply splits it to a unique identifier
# and then its needed data, perfect for importing into a database
# Step 4 - Enjoy

# Set input and output file
input_file = 'ttnome.json'
output_file = 'output.csv'

# Load JSON data from the input file
with open(input_file, 'r') as file:
    data = json.load(file)

# Open the CSV file for writing
with open(output_file, 'w', newline='') as csvfile:
    # Define the column names
    fieldnames = ['itemID', 'itemData']

    # Create a CSV writer object
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Process and write each item
    for item in data.values():
        itemID = item['itemID']
        itemData = {key: value for key, value in item.items() if key != 'itemID'}
        writer.writerow({'itemID': itemID, 'itemData': json.dumps(itemData)})