import csv

# Example of reading the products.csv file
with open('products.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Gets the header row
    products = list(csv_reader)  # Reads the rest of the data
