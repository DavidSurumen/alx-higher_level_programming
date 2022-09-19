#!/usr/bin/python3
"""Updates name of a State object in the database
hbtn_0e_6_usa."""
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

    obj = session.query(State).filter(State.id == 2)
    obj.update({"name": ("New Mexico")})

    session.commit()
