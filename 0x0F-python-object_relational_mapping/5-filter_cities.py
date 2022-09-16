#!/usr/bin/python3
"""Takes the name of a state as an arg and lists all cities
of that state."""
import MySQLdb
import sys


if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()

    cmd = """SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name=%s
            ORDER BY cities.id ASC;"""

    cur.execute(cmd, (sys.argv[4],))
    
    result = cur.fetchall()

    print(", ".join([city[0] for city in result]))

    cur.close()
    conn.close()
