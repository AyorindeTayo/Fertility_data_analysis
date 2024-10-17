SELECT Gender,
       AVG(BirthWeight) AS average_birth_weight
FROM pregnancies_and_births
JOIN individuals ON pregnancies_and_births.ChildId = individuals.IndividualId
WHERE EXTRACT(YEAR FROM OutcomeDate) BETWEEN 1997 AND 2000
  AND BirthWeight IS NOT NULL         -- Exclude null values
  AND BirthWeight >= 0                -- Exclude negative values
  AND BirthWeight < 1000              -- Example threshold for bad data, adjust as necessary
GROUP BY Gender;
