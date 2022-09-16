#!/usr/bin/python3
"""Lists all 'State' objects from the database hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3],
                                  pool_pre_ping=True))

    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State):
        print("{:d}: {}".format(instance.id, instance.name))
