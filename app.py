import pandas as pd
import psycopg2

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

# Load the Excel file
excel_file = 'FertilityData.xlsx'

# Read and upload each sheet
sheets = {
    'Individuals': {
        'dataframe': pd.read_excel(excel_file, sheet_name='Individuals'),
        'table_name': 'individuals',
        'columns': ['IndividualId', 'DoB', 'Gender', 'ObsStartDate', 'ObsEndDate']
    },
    'PregnanciesAndBirths': {
        'dataframe': pd.read_excel(excel_file, sheet_name='PregnanciesAndBirths'),
        'table_name': 'pregnancies_and_births',
        'columns': ['MotherId', 'OutcomeDate', 'Outcome', 'ChildId', 'Birthweight']
    },
    'Codebook': {
        'dataframe': pd.read_excel(excel_file, sheet_name='Codebook'),
        'table_name': 'codebook',
        'columns': ['Table Name', 'Column', 'Description', 'Domain values']
    }
}

# Step 1: Insert into Individuals table
individuals_df = sheets['Individuals']['dataframe']
individuals_table_name = sheets['Individuals']['table_name']
individuals_columns = sheets['Individuals']['columns']

for index, row in individuals_df.iterrows():
    # Ensure Gender is truncated to 1 character
    gender = str(row['Gender'])[:1]
    
    insert_query = f"""
    INSERT INTO {individuals_table_name} ({', '.join(individuals_columns)})
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (IndividualId) DO UPDATE
    SET DoB = EXCLUDED.DoB, 
        Gender = EXCLUDED.Gender, 
        ObsStartDate = EXCLUDED.ObsStartDate, 
        ObsEndDate = EXCLUDED.ObsEndDate;
    """
    
    # Replace row['Gender'] with the truncated value
    cursor.execute(insert_query, (row['IndividualId'], row['DoB'], gender, row['ObsStartDate'], row['ObsEndDate']))

# Commit changes to the individuals table
conn.commit()

# Step 2: Insert into PregnanciesAndBirths table, checking foreign key existence
pregnancies_df = sheets['PregnanciesAndBirths']['dataframe']
pregnancies_table_name = sheets['PregnanciesAndBirths']['table_name']
pregnancies_columns = sheets['PregnanciesAndBirths']['columns']

for index, row in pregnancies_df.iterrows():
    mother_id = row['MotherId']
    
    # Check if the MotherId exists in the individuals table
    cursor.execute("SELECT 1 FROM individuals WHERE IndividualId = %s", (mother_id,))
    result = cursor.fetchone()
    
    if result:
        # Ensure Outcome is truncated to 1 character
        outcome = str(row['Outcome'])[:1]
        
        # Insert if the MotherId exists in individuals table
        insert_query = f"""
        INSERT INTO {pregnancies_table_name} ({', '.join(pregnancies_columns)})
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING;
        """
        
        # Replace row['Outcome'] with the truncated value
        cursor.execute(insert_query, (mother_id, row['OutcomeDate'], outcome, row['ChildId'], row['Birthweight']))
    else:
        print(f"Skipping record with MotherId {mother_id} as it doesn't exist in individuals table.")

# Commit changes and close the connection
conn.commit()
cursor.close()
conn.close()

print("Data uploaded successfully!")
