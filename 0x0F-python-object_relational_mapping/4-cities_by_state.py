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
    cur.execute("""SELECT c.id, c.name, s.name
                   FROM cities AS c
                   JOIN states AS s ON c.state_id = s.id
                   ORDER BY id ASC;""")
    cities = cur.fetchall()

    for city in cities:
        print(city)
