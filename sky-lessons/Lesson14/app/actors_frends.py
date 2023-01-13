import sqlite3
from collections import Counter

direct = '../netflix.db'


def get_actors():
    with sqlite3.connect(direct) as con:
        cur = con.cursor()
        sqlite_query = (f"""
            SELECT netflix.cast
            FROM 'netflix'
            WHERE netflix.cast != ''
        """)
        cur.execute(sqlite_query)
        executed_query = cur.fetchall()
    return executed_query


def find_friends(first_actor, second_actor):
    all_actors = []
    friends = []
    for i in get_actors():
        if first_actor and second_actor in i[0]:
            first_list = i[0].split(',')
            actors = [i.strip() for i in first_list]
            actors.remove(first_actor)
            actors.remove(second_actor)
            all_actors += actors
    coincidence = Counter(all_actors)
    entry = coincidence.most_common()
    for i in entry:
        if i[1] > 2:
            friends.append(i[0])
    return friends


print(find_friends('Rose McIver', 'Ben Lamb'))
