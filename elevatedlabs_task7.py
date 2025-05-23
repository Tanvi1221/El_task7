# -*- coding: utf-8 -*-
"""Elevatedlabs_task7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tHzfJ4QQJoo8vJQlEafKKJnDwDpcMJze
"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('sales_data.db') #to create a connection to a database file

cursor = conn.cursor() #to create a cursor

# Create a sales table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
''')

# Insert some sample data
cursor.execute("INSERT INTO sales (product, quantity, price) VALUES ('Apple', 10, 2.5)")
cursor.execute("INSERT INTO sales (product, quantity, price) VALUES ('Banana', 20, 1.2)")
cursor.execute("INSERT INTO sales (product, quantity, price) VALUES ('Orange', 15, 1.5)")
cursor.execute("INSERT INTO sales (product, quantity, price) VALUES ('Apple', 5, 2.5)")
cursor.execute("INSERT INTO sales (product, quantity, price) VALUES ('Banana', 10, 1.2)")

conn.commit()

# Run the SQL query
query = """
SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue
FROM sales
GROUP BY product;
"""

# Load into pandas
df = pd.read_sql_query(query, conn)

df

# Plot a bar chart
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.title('Revenue by Product')
plt.ylabel('Revenue')
plt.xlabel('Product')
plt.tight_layout()
plt.show()

conn.close() #to close the connection

