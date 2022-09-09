#!/usr/bin/python3
# This script Lists all states starting with N.
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id;")
    result = cur.fetchall()
    for row in result:
        if row[1].startswith("N"):
            print(row)
    cur.close()
    db.close()
