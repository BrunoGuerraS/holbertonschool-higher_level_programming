#!/usr/bin/python3
import MySQLdb
from sys import argv


def conection():
    ''' this function connect to data base '''
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3], charset="utf8")
    except Exception:
        print("can't connect")
        return 0

    cur = db.cursor()
    instruction = "SELECT c.name FROM cities AS c JOIN states AS s ON \
    c.state_id=s.id WHERE s.name='{name}' ORDER BY c.state_id ASC"
    cur.execute(instruction.format(name=argv[4]))
    rows = cur.fetchall()
    for row in rows:
        if row != rows[-1]:
            print(row[0], end=", ")
        else:
            print(row[0], end="")
    print()
    cur.close()
    db.close()


conection()
