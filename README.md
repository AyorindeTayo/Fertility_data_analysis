


## Create a virtual Environment 
The code below shows how a virtual environment named 'witsmyenv' was created

```
python -m venv witsmyenv
```
## Activate the virtual environment 
```
witsmyenv\Scripts\activate
```

## Install Requirements
```
pip install -r requirements.txt
```


## 1.
![Imgur](https://imgur.com/GC42SQF.png)
## Importing Fertility Data into PostgreSQL Database

## Task Overview
This task aims to import data from the `FertilityData.xlsx` file into a PostgreSQL database. This file contains two main tables: `Individuals` and `PregnanciesAndBirths`, table describing the variables and their domain values.

## Steps Followed

### Step 1: Set Up PostgreSQL Database
1. **Install PostgreSQL** on my machine.
2. **Create a new database** called `wits_database` to hold the data.
```   
CREATE DATABASE wits_database;
```
### Step 2: Define Database Schema
1. Connect to PostgreSQL using the command line or a GUI tool like pgAdmin, for the assessment i connected to the PostgreSQL admin through Vscode command line,
2. **Create the necessary tables** by defining their structure:
   - Create the `Individuals` table with columns for `IndividualId`, `DoB`, `Gender`, `ObsStartDate`, and `ObsEndDate`.
   - Create the `PregnanciesAndBirths` table with columns for `MotherId`, `OutcomeDate`, `Outcome`, `ChildId`, and `Birthweight`. Ensure that `MotherId` and `ChildId` reference `IndividualId` in the `Individuals` table.


### Step 3: Prepare the Python Environment
1. Ensure that the following Python packages are installed to handle data manipulation and database interaction:
   - `pandas` for data manipulation
   - `psycopg2` for PostgreSQL interaction
   - `openpyxl` for reading Excel files

### Step 4: Load the Data Using Python
1. **Create a Python script** that connects to the PostgreSQL database.
2. Load the Excel file (`FertilityData.xlsx`) using `pandas` to read the three sheets: `Individuals`, and `PregnanciesAndBirths`
3. For each sheet:
   - Prepare an SQL `INSERT` statement to insert data into the corresponding table.
   - Use the `ON CONFLICT` clause to handle any primary key violations for the `Individuals` table, updating existing records as necessary.
   - For the `PregnanciesAndBirths` table, ensure that `MotherId` and `ChildId` exist in the `Individuals` table to avoid foreign key violations.

### Step 5: Verify Data Upload
1. After running the script, connect to PostgreSQL again to **verify that the data has been successfully uploaded**. You can query each table to see the records:
   - For `Individuals`
   - For `PregnanciesAndBirths`


### Step 6: Commit Changes
1. Make sure to commit any changes to the database after successfully uploading all the data.

### Step 7: Close Connections
1. Finally, close the database connection after completing the data upload.

## Additional Notes
- It is important to handle any potential errors, such as duplicate entries or foreign key violations, to ensure the integrity of the data being imported.
- Always secure PostgreSQL access credentials, and consider using environment variables instead of hardcoding sensitive information in scripts.
- Use tools like pgAdmin or `psql` to monitor and verify the data directly in PostgreSQL.


![Imgur](https://imgur.com/xmyGHds.png)

# 2. # Fertility Data Analysis Report

## Overview

This report provides insights into the fertility data imported from the `FertilityData.xlsx` file into the PostgreSQL database. The analysis focuses on the total population, the number of births, and the breakdown of male and female births for the years 1996 to 2000.

## Total Population

The total population recorded in the `individuals` table is as follows:

| **Total Population** |
|----------------------|
| 98,627               |

## Birth Statistics by Year
### Code
```
-- Total Population
SELECT COUNT(*) AS total_population
FROM individuals;

-- Number of Births by Year
SELECT EXTRACT(YEAR FROM OutcomeDate) AS year,
       COUNT(*) AS number_of_births,
       SUM(CASE WHEN Gender = 'M' THEN 1 ELSE 0 END) AS number_of_male_births,
       SUM(CASE WHEN Gender = 'F' THEN 1 ELSE 0 END) AS number_of_female_births
FROM pregnancies_and_births
JOIN individuals ON pregnancies_and_births.ChildId = individuals.IndividualId
WHERE EXTRACT(YEAR FROM OutcomeDate) BETWEEN 1996 AND 2000
GROUP BY year
ORDER BY year;
```

## explanation 
Purpose of the JOIN:
The goal is to retrieve information from both tables, specifically to link the ChildId in the pregnancies_and_births table to the corresponding IndividualId in the individuals table.

The following table summarizes the number of births, male births, and female births for each year from 1996 to 2000:

| **Year** | **Number of Births** | **Number of Male Births** | **Number of Female Births** |
|----------|-----------------------|----------------------------|------------------------------|
| 1996     | 1,652                 | 835                        | 816                          |
| 1997     | 1,683                 | 833                        | 846                          |
| 1998     | 1,673                 | 824                        | 849                          |
| 1999     | 1,796                 | 889                        | 902                          |
| 2000     | 1,723                 | 860                        | 861                          |

## Analysis

- The total population of 98,627 provides a comprehensive overview of the individuals recorded in the dataset.
- The birth statistics show a slight increase in the number of births from 1996 to 1999, with a peak of 1,796 births in 1999. 
- The number of male and female births is relatively balanced across the years, with a slight variation in some years.


![Imgur](https://imgur.com/UZuZz3g.png)


## Graphically representation of the table 
![Imgur](https://imgur.com/KT6lcXW.png)



# 3. Average Birth Weight by Gender (1997 - 2000)
### Code 
```
SELECT Gender,
       AVG(BirthWeight) AS average_birth_weight
FROM pregnancies_and_births
JOIN individuals ON pregnancies_and_births.ChildId = individuals.IndividualId
WHERE EXTRACT(YEAR FROM OutcomeDate) BETWEEN 1997 AND 2000
  AND BirthWeight IS NOT NULL         -- Exclude null values
  AND BirthWeight >= 0                -- Exclude negative values
  AND BirthWeight < 1000              -- Example threshold for bad data, adjust as necessary
GROUP BY Gender;
```
The following table displays the average birth weight for males and females born from 1997 to 2000. The dataset includes records with valid birth weights, excluding any bad data.

| Gender | Average Birth Weight (kg) |
|--------|---------------------------|
| F      | 2.75                      |
| M      | 2.75                      |
| Q      | 2.92                      |
| X      | 3.60                      |

**Notes:**
- The average birth weights are calculated in kilograms.
- The gender "Q" and "X" may represent additional categories that need further investigation to determine their relevance in the dataset.

![Imgur](https://imgur.com/pEtbQ9P.png)

  

#  4. Total Women with Two or More Pregnancies (1996 - 2000)

## Result

## Code
```
SELECT COUNT(*) AS total_women_with_two_or_more_pregnancies
FROM (
    SELECT MotherId
    FROM pregnancies_and_births
    WHERE EXTRACT(YEAR FROM OutcomeDate) BETWEEN 1996 AND 2000
    GROUP BY MotherId
    HAVING COUNT(*) >= 2
) AS subquery;
```

The following table displays the total number of women who experienced at least two pregnancies during the specified period:
| total_women_with_two_or_more_pregnancies |
|---------------------------------------------|
| 999                                         |

## Interpretation
This result indicates that a total of **999 women** experienced at least two pregnancies during the period from **1996 to 2000**.

![Imgur](https://imgur.com/pPpXI9L.png)
