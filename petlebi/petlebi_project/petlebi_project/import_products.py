import json
import mysql.connector
import subprocess

# Write the code to read the JSON file and insert the data into the MySQL database

# Read the JSON file
with open('petlebi_products.json', 'r', encoding='utf-8') as json_file:
    products = json.load(json_file)

#Read the create SQL statement
with open('petlebi_create.sql', 'r') as sql_file_content:
    sql_commands = sql_file_content.read()
    
#Read the insert SQL statement
with open('petlebi_insert.sql', 'r') as sql_file_content:
    insert_statement = sql_file_content.read()

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='petlebi'
)

# Create a cursor
cursor = db_connection.cursor()

try:
    cursor.execute(sql_commands)
    db_connection.commit()
    print("Table created successfully")
except mysql.connector.Error as err:
    print(f"Error: {err}")


# Insert the data into the table
for product in products:
    product_url = product['product_url']
    if product_url is not None:
        insert_query = insert_statement
        cursor.execute(insert_query, (
            product['product_name'],
            product['price'],
            product['stock'],
            product['barcode'],
            product['description'],
            product['image'],
            product['category'],
            product['brand'],
            product_url,
            product['product_id'],
            product['sku']
        ))

# Commit the changes
db_connection.commit()

# Close the connection
cursor.close()
db_connection.close()

