-- number of records with the same record

SELECT COUNT(score) AS number, score
FROM second_table
GROUP BY score;
