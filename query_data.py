import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Example: show the first 5 rows
print(" First 5 rows from 'sales' table:")
cursor.execute(" SELECT * FROM sales LIMIT 5;")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Example : Total revenue
print("\n Total revenue:")
cursor.execute("SELECT SUM (total) FROM sales;")
total_revenue= cursor.fetchone()[0]
print(f"${total_revenue:.2f}")

# Example: Revenue per product
print("\n Revenue by product:")
cursor.execute("""
    SELECT product, SUM(total) as revenue
    FROM sales
    GROUP BY product
    ORDER BY revenue DESC;
    """)
revenue_by_product = cursor.fetchall()
for product, revenue in revenue_by_product:
    print(f"{product} : $ {revenue:2f}")

# close connection 
conn.close()

