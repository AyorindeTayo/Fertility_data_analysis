SELECT COUNT(*) AS total_women_with_two_or_more_pregnancies
FROM (
    SELECT MotherId
    FROM pregnancies_and_births
    WHERE EXTRACT(YEAR FROM OutcomeDate) BETWEEN 1996 AND 2000
    GROUP BY MotherId
    HAVING COUNT(*) >= 2
    
) AS subquery;
