#!/usr/bin/python3

"""
Defines a City class which enherit from base class
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """City class with 3 attribute
    """

    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
