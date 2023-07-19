-- Lists all genres with the number of shows linked to each
-- genre and number_of_shows order by number_of_shows
SELECT g.name AS genre, COUNT(sg.genre_id) AS number_of_shows
FROM tv_genres AS g
     INNER JOIN tv_show_genres AS sg
     ON g.id = sg.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
