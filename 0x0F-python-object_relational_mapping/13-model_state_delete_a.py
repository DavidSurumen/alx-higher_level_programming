#!/usr/bin/python3
"""Deletes all 'State' objects with a name containing the
letter 'a' from the database."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3],
                                  pool_pre_ping=True))

    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State).filter(State.name.like('%a%'))

    for obj in res:
        session.delete(obj)

    session.commit()
