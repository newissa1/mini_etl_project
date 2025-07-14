import pandas as pd
import sqlite3
import os 

# To Extract 
def extract_data(filepath):
    return pd.read_csv(filepath)

# To transform 
def transform_data(df):
    # Add total price column 
    df['total']= df['quantity'] * df['price']
    df['order_date'] = pd.to_datetime(df['order_date'])
    return df 

# To Load
def load_to_sqlite(df,db_path, table_name='sales'):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists= 'replace', index= False)
    conn.close()

# Run the ETL

if __name__ == "__main__":
    file_path = 'data/sales.csv'
    db_path = 'database.db'

    if not os.path.exists(file_path):
        print("CSV file not found")

    else:
        df= extract_data(file_path)
        df_transformed= transform_data(df)
        load_to_sqlite (df_transformed, db_path)   
        print("ETL pipeline completed sucessfully")

        

