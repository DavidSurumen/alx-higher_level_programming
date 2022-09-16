#!/usr/bin/python3
"""Takes an argument and displays all values in the 'states' table
of 'hbtn_0e_0_usa' db, where 'name' matches the argument.
"""
import sys
import MySQLdb


if __name__ == '__main__':
    username = sys.argv[1]
    passw = sys.argv[2]
    db_name = sys.argv[3]
    name_search = sys.argv[4]

    conn = MySQLdb.connect(host='localhost', port=3306, user=username,
                           passwd=passw, db=db_name)
    cur = conn.cursor()

    cmd = """SELECT * FROM states
            WHERE name LIKE BINARY '{}'
            ORDER BY states.id ASC;""".format(name_search)

    cur.execute(cmd)
    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()
    conn.close()
