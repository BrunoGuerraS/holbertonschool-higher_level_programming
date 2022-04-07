#!/usr/bin/python3
import MySQLdb
from sys import argv

def conection():

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], 
                             passwd=argv[2], db=argv[3], charset="utf8")
    except Exception:
        print("can't connect")
        return 0

    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    db.close()


conection()
