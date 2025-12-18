-- List all cities of California

USE hbtn_0d_usa;
SELECT id, name FROM cities NATURAL JOIN states WHERE name = 'California' ORDER BY cities.id
