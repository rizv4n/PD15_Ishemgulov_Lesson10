import json
import sqlite3


def get_title_by_year(from_year, to_year, direct):
    with sqlite3.connect(direct) as con:
        cur = con.cursor()
        sqlite_query = (f"""
            SELECT title, release_year
            FROM 'netflix'
            WHERE release_year IN ({from_year}, {to_year})
            LIMIT 100
        """)
        cur.execute(sqlite_query)
        executed_query = cur.fetchall()
    return executed_query


def correct_result_year(result):
    final_result = []
    for i in result:
        movie = {'title': i[0], 'release_year': i[1]}
        final_result.append(movie)
    return json.dumps(final_result)
