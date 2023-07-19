-- Lists all shows whitout Comedy
SELECT s.title
FROM tv_shows AS s
     LEFT JOIN (
     	  SELECT s.id, s.title
	  FROM tv_shows as s
	       JOIN tv_show_genres AS sg
     	       ON sg.show_id = s.id
     	       JOIN tv_genres AS g
     	       ON g.id = sg.genre_id
	  WHERE g.name = 'Comedy'
	  ) AS c_shows
     ON c_shows.id = s.id
WHERE c_shows.id IS NULL
ORDER BY s.title;
