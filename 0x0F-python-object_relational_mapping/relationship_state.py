#!/usr/bin/python3
"""Contains the class definition of 'State' and an
instance Base = declarative_base()."""

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from relationship_city import Base


class State(Base):
    """State model."""
    __tablename__ = 'states'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="states_")
