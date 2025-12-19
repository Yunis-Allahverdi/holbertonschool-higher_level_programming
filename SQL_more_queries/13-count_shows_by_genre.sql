-- List all genres and num of shows linked to each

SELECT tv_genres.`name` as genre, COUNT(DISTINCT tv_shows.`id`) DESC AS number_of_shows
FROM `tv_shows`
INNER JOIN `tv_show_genres`
ON tv_shows.`id` = tv_show_genres.`show_id`;
