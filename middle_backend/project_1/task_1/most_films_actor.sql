-- решение mxmaslin

SELECT
    name ,
    max (caid)
from (
    select
        a.name as name, 
        count(m.id) caid
    from
        actors a
    join
        movie_actors ma
        on ma.actor_id = a.id
    join
        movies m
        on m.id = ma.movie_id
    WHERE
        name != 'N/A'
    GROUP by
        name
)

-- решение авторов курса

SELECT
    count(actors.id) cnt,
    actors.name
FROM
    actors
INNER JOIN
    movie_actors ON (movie_actors.actor_id = actors.id)
WHERE
    actors.name != 'N/A'
GROUP BY
    actors.id
ORDER BY
    cnt DESC limit 1; 
