CREATE DATABASE hbtn_0d_tvshows;

mysql -u root -p hbtn_0d_tvshows < hbtn_0d_tvshows.sql

USE hbtn_0d_tvshows;

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
