-- решение mxmaslin

select 
    name
from
    actors a
JOIN
    movie_actors ma
    on ma.actor_id = a.id
JOIN
    movies m
    on m.id = ma.movie_id
WHERE
    m.director like '%Jørgen Lerdam%'

-- решение авторов курса

SELECT
    a.name
FROM
    movies m
INNER JOIN
    movie_actors ma
    ON ma.movie_id=m.id
INNER JOIN
    actors a
    ON ma.actor_id=a.id
WHERE
    m.director LIKE '%Jørgen Lerdam%';
