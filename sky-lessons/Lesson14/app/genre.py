import json
import sqlite3


def get_title_by_genre(genre, direct):
    with sqlite3.connect(direct) as con:
        cur = con.cursor()
        sqlite_query = (f"""
            SELECT title, description
            FROM 'netflix'
            WHERE listed_in LIKE '%{genre}%'
            AND date_added != ''
            ORDER BY date_added DESC
        """)
        cur.execute(sqlite_query)
        executed_query = cur.fetchall()
    return executed_query


def correct_result_genre(result):
    final_result = []
    for i in range(10):
        movie = {'title': result[i][0], 'description': result[i][1]}
        final_result.append(movie)
    return json.dumps(final_result)

