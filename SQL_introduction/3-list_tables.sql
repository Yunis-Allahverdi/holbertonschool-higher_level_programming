-- Show 3 tables based on given database mysql
SELECT table_name FROM information_schema.tables WHERE table_schema = 'mysql' and table_type='BASE TABLE' LIMIT 3;

