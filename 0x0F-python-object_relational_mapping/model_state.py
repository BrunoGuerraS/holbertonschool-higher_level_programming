#!/usr/bin/python3
'''
Models States inherits from  base
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    ''' class State '''

    __tablenames__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
