-- script that lists all cities --
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.id = states.id
ORDER BY cities.id;
