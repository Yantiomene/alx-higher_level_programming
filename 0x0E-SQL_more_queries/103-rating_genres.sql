-- Lists all genre by their rating
SELECT g.name, SUM(r.rate) AS rating
FROM tv_genres AS g
     JOIN tv_show_genres AS gs
     ON g.id = gs.genre_id
     JOIN tv_show_ratings AS r
     ON r.show_id = gs.show_id
GROUP BY g.name
ORDER BY rating DESC;
