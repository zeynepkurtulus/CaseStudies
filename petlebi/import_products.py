import json
import mysql.connector

# Read JSON data
with open('petlebi_products.json') as json_file:
    products = json.load(json_file)

# Connect to MySQL
connection = mysql.connector.connect(
    host='your_host',
    user='your_user',
    password='your_password',
    database='your_database'
)

cursor = connection.cursor()

# Insert data into the 'petlebi' table
for product in products:
    query = """
    INSERT INTO petlebi (product_url, product_name, product_barcode, product_price)
    VALUES (%s, %s, %s, %s)
    """
    values = (
        product['product_url'],
        product['product_name'],
        product['product_barcode'],
        product['product_price']
    )
    cursor.execute(query, values)

connection.commit()
connection.close()
