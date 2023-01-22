#!/usr/bin/python3
"""Creates the State 'California' with City 'San Francisco'
in the database hbtn_0e_6_usa."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from relationship_city import City
from relationship_state import State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3],
                                  pool_pre_ping=True)
                           )

    Session = sessionmaker(bind=engine)
    session = Session()

    carl = State(name="California")
    carl.cities = City(name="San Francisco")

    session.add(carl)
    session.commit()
