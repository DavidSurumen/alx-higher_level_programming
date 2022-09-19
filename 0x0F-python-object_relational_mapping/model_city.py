#!/usr/bin/python3
"""Contains the class 'City'."""
from model_state import Base, State
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """City definition."""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
