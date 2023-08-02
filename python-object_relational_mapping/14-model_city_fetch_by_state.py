#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""

from model_state import Base, State
from model_city import City
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

    cities = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
