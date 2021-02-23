SQL_QUERY = """
    select
        m.id,
        cast(m.imdb_rating as float) imdb_rating,
        m.genre,
        m.title,
        m.plot description,
        m.director,
        a.id actor_id,
        a.name,
        m.writer movie_writer,
        m.writers movie_writers,
        w.id writer_id,
        w.name writer_name
    from
        movies as m
    left join
        movie_actors ma
        on ma.movie_id = m.id
    left join
        actors a
        on a.id = ma.actor_id
    left join
        writers w
        on w.id == m.writer or m.writers like '%' | w.name | '%'
    order by
        1;
"""