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
        new_state = State("Louisiana")
        session.add(new_state)
        session.commit()
    finally:
        session.close()

    rows = session.query(State).filter(State.name == "Louisiana")

    print(rows[0].id)

    session.close()
