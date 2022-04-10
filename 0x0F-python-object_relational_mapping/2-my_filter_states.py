#!/usr/bin/python3
''' we start to work with MySQLdb to handle data bases'''


def conection():
    ''' this function connect to databae '''

    import MySQLdb
    from sys import argv

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3], charset="utf8")
    except Exception:
        print("can't connect")
        return 0

    cur = db.cursor()
    instruc = "SELECT * FROM states WHERE BINARY name=%s ORDER BY id"
    cur.execute(instruc, (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    conection()
