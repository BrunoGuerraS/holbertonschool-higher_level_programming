#!/usr/bin/python3
"""
Start database
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    """
    Conect and quering database
    """
    sql = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(sql.format(argv[1],
                                      argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    try:
        get_query = session.query(State.id, State.name).first()
        print("{}: {}".format(get_query.id, get_query.name))
    except Exception:
        print("Nothing")
    session.close()
