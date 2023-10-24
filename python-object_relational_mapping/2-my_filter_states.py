#!/usr/bin/python3
"""Takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument."""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cur()
    cur.execute("""
        SELECT *
        FROM states
        WHERE name LIKE '{}'
        ORDER BY states.id
    """.format(sys.argv[4]))

    results = cur.fetchall()

    for state in results:
        print(state)

    cur.close()
    db.close()
