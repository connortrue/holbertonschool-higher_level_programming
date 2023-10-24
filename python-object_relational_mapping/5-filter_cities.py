#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    query = '''SELECT *
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC;
            '''
    c.execute(query)

    cities = c.fetchall()

    p_cities = [city[2] for city in cities if city[4] == sys.argv[4]]
    print(', '.join(p_cities))

    c.close()
    db.close()
