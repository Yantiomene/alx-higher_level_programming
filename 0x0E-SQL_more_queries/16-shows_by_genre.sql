-- Lists all shows and genres
SELECT s.title, g.name
FROM tv_shows AS s
     LEFT JOIN tv_show_genres AS sg
     ON sg.show_id = s.id
     LEFT JOIN tv_genres AS g
     ON g.id = sg.genre_id
ORDER BY s.title, g.name;
