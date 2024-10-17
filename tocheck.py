import psycopg2
import pandas as pd

# PostgreSQL connection parameters
db_params = {
    'dbname': 'wits_database',        # Change to your PostgreSQL database name
    'user': 'olanipekunayo2012@gmail.com',  # Change to your PostgreSQL username
    'password': 'Ayorinde123%',      # Change to your PostgreSQL password
    'host': '127.0.0.1',
    'port': '5432'
}

# Connect to PostgreSQL
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# Function to check the contents of a table
def check_table(table_name):
    query = f"SELECT * FROM {table_name} LIMIT 5;"  # Retrieve the first 5 rows
    cursor.execute(query)
    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    
    # Print the results
    if rows:
        print(f"\nTable: {table_name}")
        df = pd.DataFrame(rows, columns=column_names)
        print(df)
    else:
        print(f"\nTable: {table_name} is empty or does not exist.")

# List of tables to check
tables = ['individuals', 'pregnancies_and_births', 'codebook']

# Check each table for data
for table in tables:
    check_table(table)

# Close the connection
cursor.close()
conn.close()
