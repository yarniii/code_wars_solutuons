SELECT DATE(created_at) as day, description, COUNT(name) as count FROM events
WHERE name LIKE '%trained%'
GROUP BY day,description
ORDER by day;
