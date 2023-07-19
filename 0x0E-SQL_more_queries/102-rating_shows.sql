-- Lists all shows by their ratings
SELECT s.title, SUM(r.rate) AS rating
FROM tv_shows AS s
     JOIN tv_show_ratings AS r
     ON s.id = r.show_id
GROUP BY s.title
ORDER BY rating DESC;
