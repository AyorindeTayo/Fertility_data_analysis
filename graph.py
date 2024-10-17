import pandas as pd
import matplotlib.pyplot as plt
import psycopg2

# PostgreSQL connection parameters
db_params = {
    'dbname': 'wits_database',
    'user': 'olanipekunayo2012@gmail.com',
    'password': 'Ayorinde123%',
    'host': '127.0.0.1',
    'port': '5432'
}

# Connect to PostgreSQL
conn = psycopg2.connect(**db_params)
query = """
    SELECT EXTRACT(YEAR FROM OutcomeDate) AS year,
           COUNT(*) AS number_of_births,
           SUM(CASE WHEN Gender = 'M' THEN 1 ELSE 0 END) AS number_of_male_births,
           SUM(CASE WHEN Gender = 'F' THEN 1 ELSE 0 END) AS number_of_female_births
    FROM pregnancies_and_births
    JOIN individuals ON pregnancies_and_births.ChildId = individuals.IndividualId
    WHERE EXTRACT(YEAR FROM OutcomeDate) BETWEEN 1996 AND 2000
    GROUP BY year
    ORDER BY year;
"""

# Load data into a DataFrame
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Plotting the data
plt.figure(figsize=(10, 6))

# Plotting total births
plt.bar(df['year'], df['number_of_births'], color='gray', label='Total Births')

# Plotting male births
plt.bar(df['year'], df['number_of_male_births'], color='blue', label='Male Births', alpha=0.7)

# Plotting female births
plt.bar(df['year'], df['number_of_female_births'], color='pink', label='Female Births', alpha=0.7)

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Number of Births')
plt.title('Births by Year (1996 - 2000)')
plt.legend()
plt.xticks(df['year'])

# Save the plot
plt.savefig('births_by_year_1996_2000.png')  # Change the filename and format as needed

# Show the plot
plt.show()
