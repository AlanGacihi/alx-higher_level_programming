#!/usr/bin/python3
# This script Lists states with a given name.
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id;"
                .format(sys.argv[4]))
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    db.close()
