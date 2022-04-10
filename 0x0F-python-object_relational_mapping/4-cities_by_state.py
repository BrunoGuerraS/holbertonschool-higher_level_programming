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
    inst1 = "SELECT cities.id, cities.name, states.name FROM cities "
    inst2 = "LEFT JOIN states ON cities.state_id = states.id"
    cur.execute(inst1 + inst2)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


conection()
