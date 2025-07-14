import streamlit as st
import pandas as pd
import sqlite3

# Connect to the  SQlite database
conn= sqlite3.connect('database.db')

# Load the sales table to the database
df= pd.read_sql_query("SELECT * FROM sales", conn)

# Close the connection
conn.close()

#streamlit dashboard
st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("Sales Dashboard")


# show raw data
st.subheader("Raw Sales Data")
st.dataframe(df)

# Total revenue
total_revenue = df["total"].sum()
st.metric("Total revenue", f"${total_revenue:,.2f}")


#Revenue by product
st.subheader("Revenue by Product")
revenue_product= df.groupby("product")["total"].sum().sort_values(ascending=False)
st.bar_chart(revenue_product)

#Revenue by customer
st.subheader("Revenue by Customer")
revenue_customer_name= df.groupby("customer_name")["total"].sum().sort_values(ascending=False)
st.bar_chart(revenue_customer_name)
