#!/usr/bin/python3
"""Takes in an argument and displays all values in the states table"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    state_name = sys.argv[4]
    cur = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id"
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
