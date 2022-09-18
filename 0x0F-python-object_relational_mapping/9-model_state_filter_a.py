#!/usr/bin/python3
"""Lists all 'State' objects that contain the letter 'a'
from the database hbtn_0e_6_usa."""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3],
                                  pool_pre_ping=True))

    Session = sessionmaker(bind=engine)
    session = Session()

    objs = session.query(State).filter(State.name.like('%a%'))
    for obj in objs:
        print('{:d}: {}'.format(obj.id, obj.name))
