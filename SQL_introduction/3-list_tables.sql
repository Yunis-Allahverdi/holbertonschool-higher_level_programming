-- Show 3 tables based on given database mysql

SELECT * FROM information_schema.tables 
WHERE table_schema = 'mysql' LIMIT 3;

