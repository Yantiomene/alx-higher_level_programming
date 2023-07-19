-- List all genre of not linked to the show Dexter
SELECT g.name
FROM tv_genres AS g
     LEFT JOIN (
     	  SELECT g.id, g.name		-- SELECT ALL Dexter genre
	  FROM tv_genres AS g
	       JOIN tv_show_genres AS sg
     	       ON g.id = sg.genre_id
     	       JOIN tv_shows AS s
     	       ON sg.show_id = s.id
	  WHERE s.title = 'Dexter'
	  ) AS d_genres ON d_genres.id = g.id
WHERE d_genres.id IS NULL			-- Exclude Dexter Genre
ORDER BY g.name;
