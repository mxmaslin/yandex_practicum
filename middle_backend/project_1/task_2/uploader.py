import sqlite3
from itertools import groupby
from pprint import pprint

from sql_query import SQL_QUERY

conn = sqlite3.connect('db.sqlite')

executed = conn.execute(SQL_QUERY)
records = executed.fetchall()
records = sorted(records, key=lambda x: x[0])

parsed_movies = []

for key, group_items in groupby(records, key=lambda x: x[0]):
    parsed_movie = {}
    parsed_movie['id'] = key
    actors_names = set()
    writers_names = set()
    actors = []
    writers = []
    for movie_unit in group_items:
        (the_id, imdb_rating, genre, title, description, director, actor_id,
         actor_name, movie_writer, movie_writers, writer_id, writer_name) = movie_unit
        actors_names.add(actor_name)
        parsed_movie['imdb_rating'] = imdb_rating
        parsed_movie['genre'] = genre
        parsed_movie['title'] = title
        parsed_movie['description'] = None if description == 'N/A' else description
        parsed_movie['director'] = None if director == 'N/A' else director
        if actor_name and actor_name != 'N/A':
            actors_names.add(actor_name)
            actors_values = [list(x.values())[0] for x in actors]
            if actor_name not in actors_values:
                actors.append({the_id: actor_name})
        if writer_name and writer_name != 'N/A':
            writers_names.add(writer_name)
            writers_values = [list(x.values())[0] for x in writers]
            if writer_name not in writers_values:
                writers.append({the_id: writer_name})
    actors_names = ', '.join(actors_names)
    parsed_movie['actors_names'] = actors_names
    parsed_movie['actors'] = actors
    writers_names = ', '.join(writers_names)
    parsed_movie['writers_names'] = writers_names
    parsed_movie['writers'] = writers
    parsed_movies.append((parsed_movie))

pprint(parsed_movies)
