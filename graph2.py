import pandas as pd
import matplotlib.pyplot as plt
import psycopg2
import numpy as np

# PostgreSQL connection parameters
db_params = {
    'dbname': 'wits_database',
    'user': 'olanipek.com',
    'password': 'Ayo',
    'host': '127.0.0',
    'port': '52'
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

# Set bar width
bar_width = 0.35

# Set positions for each bar
r1 = np.arange(len(df['year']))  # Positions for total births
r2 = [x + bar_width for x in r1]  # Positions for male births
r3 = [x + bar_width for x in r2]  # Positions for female births

# Plotting total births
plt.bar(r1, df['number_of_births'], color='gray', width=bar_width, label='Total Births')

# Plotting male births
plt.bar(r2, df['number_of_male_births'], color='blue', width=bar_width, label='Male Births')

# Plotting female births
plt.bar(r3, df['number_of_female_births'], color='pink', width=bar_width, label='Female Births')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Number of Births')
plt.title('Births by Year (1996 - 2000)')
plt.xticks([r + bar_width for r in range(len(df['year']))], df['year'])  # Centering the x-ticks
plt.legend()

# Save the plot
plt.savefig('births_by_year_1996_2000_separate.png')  # Change the filename and format as needed

# Show the plot
plt.show()
