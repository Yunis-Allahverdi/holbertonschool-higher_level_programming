-- number of records with the same record

SELECT score, COUNT(score) DESC AS number
FROM second_table
GROUP BY score;
