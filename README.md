# CaseStudies
Case studies that I conducted for various internship and job applications. Below are th descriptions of the case studies:

# Petlebi Case Study ~ Jeton Digital: Web Scrapping using Python
Assignment is as below;
Extract all the products on www.petlebi.com and create a JSON file. The attributes required for the products to be drawn are as follows. If you can't access any of these, leave it blank as the "Attribute" field, even if it is empty in the JSON. The "Attributes" are as follows:
- product URL
- product name
- product barcode
- product price
- product stock
- product images
- description
- sku
- category
- product ID
- brand
Use 'Python' when doing this 'web scraping'. (Library to use: https://scrapy.org/). Then write the JSON file you created to a table named 'petlebi' in a MySQL database. Again, do this with python. The files you need to submit at the end of the task are as follows;
- petlebi_scrapy.py (py file for web scraping) — Executing this file should write data to JSON
- petlebi_products.json (data obtained as JSON) — The data we print here should be viewable in a Text Editor.
- import_products.py (PY file that writes from the JSON file to the petlebi table in the MySQL database) — When this file is run, the data in the JSON should be written to the database.
- petlebi_create.sql (sql output that creates the petlebi table, hint: SQL file containing the sql statement that starts with the CREATE command) — When this file is run, a table named 'petlebi' should be created in the database
- petlebi_insert.sql (SQL file containing the INSERT statements of the data you have written to the petlebi table) — When this file is run, data should be able to be inserted into the table created in the next step as 'petlebi'.

