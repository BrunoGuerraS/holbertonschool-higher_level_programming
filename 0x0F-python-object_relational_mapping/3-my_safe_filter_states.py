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
    instructions = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cur.execute(instructions, (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    db.close()


conection()
