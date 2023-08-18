#!/usr/bin/python3

"""
script to fetch all states from the database
"""

from sqlalchemy import (create_engine)
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).\
        filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)

    session.commit()
