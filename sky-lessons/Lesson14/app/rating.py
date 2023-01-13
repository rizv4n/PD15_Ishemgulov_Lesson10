import json
import sqlite3


def get_title_by_rating(rating_list, direct):
    with sqlite3.connect(direct) as con:
        cur = con.cursor()
        sqlite_query = (f"""
            SELECT title, rating, description
            FROM 'netflix'
            WHERE rating IN {rating_list}
            LIMIT 100
        """)
        cur.execute(sqlite_query)
        executed_query = cur.fetchall()
    return executed_query


def correct_result_rating(result):
    final_result = []
    for i in result:
        movie = {'title': i[0], 'rating': i[1], 'description': i[2]}
        final_result.append(movie)
    return json.dumps(final_result)
