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

    new_object = State(name="Louisiana")

    session = Session(engine)

    session.add(new_object)

    session.commit()

    print(new_object.id)
