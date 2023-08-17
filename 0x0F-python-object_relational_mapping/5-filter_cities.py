#!/usr/bin/python3

"""
List all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("""SELECT c.name
                   FROM cities AS c
                   JOIN states AS s ON c.state_id = s.id
                   WHERE s.name = %s
                   ORDER BY c.id ASC;""", (sys.argv[4],))
    cities = cur.fetchall()

    cities = [c[0] for c in cities]

    for i in range(0, len(cities)):
        if i < len(cities) - 1:
            print(cities[i], end=", ")
    print(cities[i])
