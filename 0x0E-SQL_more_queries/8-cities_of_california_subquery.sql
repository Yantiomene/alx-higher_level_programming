-- Lists all cityies of California and sort by cities id
SELECT c.id, c.name
FROM cities AS c, states AS s
WHERE c.state_id = s.id and s.name = 'California'
ORDER BY c.id;
