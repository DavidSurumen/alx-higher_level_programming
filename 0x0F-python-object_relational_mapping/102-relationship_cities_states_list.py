#!/usr/bin/python3
""" Lists all City objects from the database, using 'state'
relationship to access the State object linked to the City object."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City, State).order_by(City.id).filter(
            City.state_id == State.id):
        print('{}: {} -> {}'.format(city.City.id,
                                    city.City.name,
                                    city.State.name))
