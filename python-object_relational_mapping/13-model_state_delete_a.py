#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys


if __name__ == "__main__":
    # Create an instance of SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:\
                            3306/{}'.format(sys.argv[1],
                                            sys.argv[2],
                                            sys.argv[3]))

    session = Session(engine)

    states = session.query(State).filter(State.name.like("%a%"))\
        .order_by(State.id).all()

    for state in states:
        session.delete(state)

    session.commit()
