#!/usr/bin/python3
''' we start to work with MySQLdb to handle data bases'''
import MySQLdb
from sys import argv


def conection():
    ''' this function connect to databae '''
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
        if row[1] == argv[4] and row[1][0] == 'A':
            print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    conection()

