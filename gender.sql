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
