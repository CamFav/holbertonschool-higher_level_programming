#!/usr/bin/python3
"""Takes in an argument and displays all values in the states table"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    state_name = sys.argv[4]
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states \
                ON states.id = cities.state_id WHERE states.name = '{}'"
            .format(state_name)
            )
    rows = cur.fetchall()
    cities_list = []
    for row in rows:
        cities_list.append(row[0])
    cities_str = ", ".join(cities_list)
    print(cities_str)
    cur.close()
    db.close()
