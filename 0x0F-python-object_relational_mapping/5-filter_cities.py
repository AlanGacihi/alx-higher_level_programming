#!/usr/bin/python3
# Takes in the name of a state as argument and lists all cities of that state.
# And it is safe of SQL injection.
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id\
                = states.id WHERE states.name LIKE BINARY %s ORDER BY\
                cities.id;", (sys.argv[4], ))
    result = cur.fetchall()
    l = []
    for row in result:
        l.append(row[0])
    print(", ".join(l))
    cur.close()
    db.close()
