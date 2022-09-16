#!/usr/bin/python3
"""Script that lists all 'states' whose name starts with 'N',
from database"""
import MySQLdb
import sys


if __name__ == "__main__":
    user_name = sys.argv[1]
    passw = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(host='localhost', port=3306, user=user_name,
                           passwd=passw, db=db_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
    
    query_res = cur.fetchall()
    for row in query_res:
        print(row)

    cur.close()
    conn.close()
