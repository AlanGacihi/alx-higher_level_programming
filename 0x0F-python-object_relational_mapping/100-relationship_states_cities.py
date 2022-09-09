#!/usr/bin/python3
""" Inserts California state and San Francisco city. """
import sys
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    New_state = State(name="California")
    session.add(New_state)
    session.commit()
    New_city = City(name="San Francisco", state_id=New_state.id)
    session.add(New_city)
    session.commit()
    session.close()
