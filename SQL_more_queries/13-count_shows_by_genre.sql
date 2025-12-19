-- List all genres and num of shows linked to each

SELECT tv_genres.name as genre, COUNT(*) 
FROM (
    SELECT tv_shows.id
    FROM tv_shows
    INNER JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id
    GROUP BY tv_shows.id
) AS shows;
