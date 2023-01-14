import sqlite3
import json

direct = '../netflix.db'


def get_results(element_type, year, genre):
    with sqlite3.connect(direct) as con:
        cur = con.cursor()
        sqlite_query = (f"""
            SELECT title, description, listed_in
            FROM 'netflix'
            WHERE type == '{element_type}'
            AND release_year == {year}
            AND listed_in LIKE '%{genre}%'
        """)
        cur.execute(sqlite_query)
        executed_query = cur.fetchall()
    return json.dumps(executed_query)


print(get_results('TV Show', 2021, 'dramas'))
