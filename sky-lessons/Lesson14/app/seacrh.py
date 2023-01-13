import json
import sqlite3


def get_title_by_word(text, direct):
    with sqlite3.connect(direct) as con:
        cur = con.cursor()
        sqlite_query = (f"""
            SELECT title, country, release_year, description
            FROM 'netflix'
            WHERE title LIKE '%{text}%'
            AND date_added != ''
            ORDER BY date_added DESC
        """)
        cur.execute(sqlite_query)
        executed_query = cur.fetchall()
    return executed_query[0]


def correct_result_title(result):
    final_result = {'title': result[0], 'country': result[1], 'release_year': result[2], 'description': result[3]}
    return json.dumps(final_result)
