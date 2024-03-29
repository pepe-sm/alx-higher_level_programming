#!/usr/bin/python3
""" cities by state """

import MySQLdb
from sys import argv


def cities_st():
    """ cities inner join state """

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities INNER JOIN states ON \
                cities.state_id=states.id ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    db.close()

if __name__ == '__main__':
    cities_st()
