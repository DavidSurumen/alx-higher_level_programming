#!/usr/bin/python3
"""Lists all 'cities' from the database 'hbtn_0e_4_usa'"""
import MySQLdb
import sys


if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])

    cur = conn.cursor()
    cmd = """SELECT cities.id, cities.name, states.name
            FROM states
            JOIN cities ON states.id = cities.state_id
            ORDER BY id ASC;"""

    cur.execute(cmd)
    res = cur.fetchall()
    for row in res:
        print(row)

    cur.close()
    conn.close()
