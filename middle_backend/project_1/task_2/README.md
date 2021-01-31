# ETL-механизм загрузки фильмов

Реализуйте ETL-механизм загрузки фильмов из SQLite в Elasticsearch. Основная задача — написать SQL-запрос в SQLite для получения фильмов и всех связанных сущностей, затем трансформировать данные и загрузить их в индекс movies в Elasticsearch.

**Входные данные**:

- Таблицы в [БД](db.sqlite) SQLite, на которые нужно опираться при запросах: `movies`, `movie_actors`, `actors`, `writers`.
- [Схема данных](movies_index_db_scheme.json) индекса `movies`, в которую должна производиться загрузка фильмов.
- [Тесты Postman](postman_tests.json) для проверки правильности решения.

**Подсказка**

Чтобы всё получилось, проверьте:
- удалены ли все `N/A`-записи у `actors`, `actors_names`, `writers` и `writers_names`;
- нет ли дублей;
- заменены ли `N/A`-записи на `None` в `description` и `director` ;
- имеет ли поле `imdb_rating` тип `float`.

[**Решение**](uploader.py)
