-- number of records with the same record

SELECT score, COUNT(score) AS number
FROM second_table DESC
GROUP BY score;
