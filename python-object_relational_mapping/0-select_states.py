#!/usr/bin/python3
"""Get all states"""
import MySQLdb
import sys


if __name__ == '__main__':
    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            database=sys.argv[3]
    )
    
    cur = connection.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cur:
        print(row)

    cur.close()
    connection.close()
