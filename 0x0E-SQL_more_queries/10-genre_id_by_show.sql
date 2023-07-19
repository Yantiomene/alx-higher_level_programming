-- Lists all shows with at least one genre linked.
-- tv_shows.title and tv_show_genres.genre_id ORDER
SELECT s.title, g.genre_id
FROM tv_shows AS s, tv_show_genres AS g
WHERE g.show_id = s.id
ORDER BY s.title, g.genre_id;
