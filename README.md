# Part A

## Question 1. Table Analysis

The following table contains details of individuals, their year of birth, and their parents:

| Name    | Year of Birth | Father          | Mother               |
|---------|---------------|-----------------|----------------------|
| William | 1959          | Bright Mabunda  | Busi Khosa           |
| Walter  | 1962          | Bright Mabunda  | Busi Khosa           |
| Valies  | 1963          | Bens Mabunda    | Thandeka Nyalungu    |
| Suzan   | 1962          | Bens Mabunda    | Busi Khosa           |

### Observations

1. **Two Fathers for Children Born in 1962**:
   - Both *Walter* and *Suzan* were born in 1962, but they have different fathers: *Walter*'s father is listed as **Bright Mabunda**, while *Suzan*'s father is **Bens Mabunda**. This suggests potential inconsistencies in the data or could indicate a more complex family structure.

2. **Shared Mother with Different Fathers**:
   - *Busi Khosa* is listed as the mother of *William*, *Walter*, and *Suzan*. However, the father of *William* and *Walter* is **Bright Mabunda**, while the father of *Suzan* is **Bens Mabunda**. This could be an error or indicate that *Busi Khosa* had children with two different partners.

3. **Potential Data Inconsistencies**:
   - *Suzan*'s parentage is particularly unusual since her father is listed as **Bens Mabunda**, but her mother is *Busi Khosa*, who is also the mother of *William* and *Walter*. 
   - This could indicate either a data entry error or a scenario where *Busi Khosa* had children with both **Bright Mabunda** and **Bens Mabunda**.

### Conclusion

The key inconsistency is that children born around the same time (1962) have different fathers, and one mother (Busi Khosa) seems to have children with two different partners. It might indicate some complex family relationships or possible data entry issues.


## Question 2: Analysis of Identity Numbers

The following table contains identity numbers with check digits, as well as the year of birth and parent identity numbers:

| IndividualId | YearOfBirth | FatherId   | MotherId   |
|--------------|-------------|------------|------------|
| 101010-1     | 1926        | 172463-1   | 176464-2   |
| 120963-3     | 1933        | 193741-2   | 120963-3   |
| 131044-5     | 1930        | 1722A3-4   | 197651-2   |
| 137249-7     | 1936        | 101010-1   | 139724-3   |
| 134572-9     | 1948        | 129374-2   | 172463-1   |
| 149323-2     | 1938        | 101010-2   | 147263-5   |
| 155421-3     | 1995        | 14726-5    | 139724-3   |

### Observations

1. **Invalid Character in FatherId:**
   - In the third row, the `FatherId` is listed as `1722A3-4`. The presence of the letter **"A"** in a numerical identity field is unusual and could indicate a data entry error or misformatted identifier.

2. **Repetition of IndividualId and MotherId:**
   - In the second row, the `IndividualId` (120963-3) and `MotherId` (120963-3) are identical, which is unusual. It suggests that the individual's mother is listed as the individual themselves, which is biologically and logically impossible.

3. **FatherId Format Issue:**
   - In the last row, the `FatherId` is listed as `14726-5`, which is a 5-digit number instead of the expected 6 digits. This could indicate a missing digit or an incorrectly formatted ID.

4. **Check Digit Consistency:**
   - Each individual ID is paired with a check digit after the dash (`-`). The consistency of these check digits should be verified through a predefined check digit validation rule, which seems to be missing or improperly applied for some entries.

5. **Parentage Links:**
   - In several rows, the same `FatherId` (e.g., `101010-1`) is listed for different individuals, suggesting that these individuals share the same father. However, inconsistencies in the formatting and structure of other `FatherId` entries raise concerns about data integrity.

### Conclusion

There are a few data irregularities, including:
- The use of a non-numeric character in a field expected to contain only numbers.
- A scenario where an individual is listed as their own mother.
- Variations in the number of digits for `FatherId`.
- The check digit consistency needs to be validated across the dataset.

These issues suggest potential data entry errors or the need for further data cleaning and validation.


# Part B
## 1.
![Imgur](https://imgur.com/GC42SQF.png)
# Importing Fertility Data into PostgreSQL

## Task Overview
The goal of this task is to import data from the `FertilityData.xlsx` file into a PostgreSQL database. This file contains two main tables: `Individuals` and `PregnanciesAndBirths`, table describing the variables and their domain values.

## Steps Followed

### Step 1: Set Up PostgreSQL Database
1. **Install PostgreSQL** on your machine if it is not already installed.
2. **Create a new database** called `wits_database` to hold the data.

### Step 2: Define Database Schema
1. Connect to PostgreSQL using the command line or a GUI tool like pgAdmin.
2. **Create the necessary tables** by defining their structure:
   - Create the `Individuals` table with columns for `IndividualId`, `DoB`, `Gender`, `ObsStartDate`, and `ObsEndDate`.
   - Create the `PregnanciesAndBirths` table with columns for `MotherId`, `OutcomeDate`, `Outcome`, `ChildId`, and `Birthweight`. Ensure that `MotherId` and `ChildId` reference `IndividualId` in the `Individuals` table.
   - Create the `Codebook` table to describe the variables and their domain values.

### Step 3: Prepare the Python Environment
1. Ensure that the following Python packages are installed to handle data manipulation and database interaction:
   - `pandas` for data manipulation
   - `psycopg2` for PostgreSQL interaction
   - `openpyxl` for reading Excel files

### Step 4: Load the Data Using Python
1. **Create a Python script** that connects to the PostgreSQL database.
2. Load the Excel file (`FertilityData.xlsx`) using `pandas` to read the three sheets: `Individuals`, `PregnanciesAndBirths`, and `Codebook`.
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
The following table displays the average birth weight for males and females born during the period from 1997 to 2000. The dataset includes records with valid birth weights, excluding any bad data.

| Gender | Average Birth Weight (kg) |
|--------|---------------------------|
| F      | 2.75                      |
| M      | 2.75                      |
| Q      | 2.92                      |
| X      | 3.60                      |

**Notes:**
- The average birth weights are calculated in kilograms.
- The gender "Q" and "X" may represent additional categories that need further investigation to determine their relevance in the dataset.

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


