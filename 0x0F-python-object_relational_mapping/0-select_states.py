#!/usr/bin/python3
"""Script that lists all 'states' from database"""
import MySQLdb
import sys


if __name__ == '__main__':
    user_name = sys.argv[1]
    passw = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=user_name, passwd=passw, db=db_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
