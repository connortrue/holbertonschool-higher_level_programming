#!/usr/bin/python3
"""Script that lists all State objects that contain the letter a from the
 database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Setup connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Link to our engine
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for states containing the letter 'a'
    states = session.query(State).filter
    (State.name.contains('a')).order_by(State.id)

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
