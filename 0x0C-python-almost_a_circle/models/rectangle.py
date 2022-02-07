#!/usr/bin/python3
from base import Base
''' we create a class reactangle'''


class Rectangle(Base):
   ''' class rectangle'''
   def __init__(self, width, height, x=0, y=0, id=None):
       ''' constructor method'''
       super().__init__(id)
       self.width = width
       self.height = height
       self.x = x
       self.y = y


