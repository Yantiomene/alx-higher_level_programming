-- Lists all records with a name value and order by score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
