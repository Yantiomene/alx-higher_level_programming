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
    cur.execute("""SELECT * FROM states
                   WHERE CONVERT(`name` USING Latin1)
                   COLLATE Latin1_General_CS
                   LIKE 'N%';""")
    states = cur.fetchall()

    for state in states:
        print(state)
