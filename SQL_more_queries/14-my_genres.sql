-- List all genres of the show DEXTER

SELECT DISTINCT tv_genres.name AS name FROM tv_genres JOIN tv_shows WHERE tv_shows.title = 'Dexter' ORDER BY tv_genres.name;
