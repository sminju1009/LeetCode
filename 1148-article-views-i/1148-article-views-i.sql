SELECT author_id as id
FROM views
GROUP BY author_id, viewer_id
HAVING author_id=viewer_id
ORDER BY id;