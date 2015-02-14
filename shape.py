#!/usr/bin/env python3

import sys
import os
import math

class Shape:
    """Shape class: has method move"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, deltaX, deltaY):
        self.x = self.x + deltaX
        self.y = self.y + deltaY
    
class Square(Shape):
    """Square Class: inherits from Shape"""
    def __init__(self, side=1, x=0, y=0):
        Shape.__init__(self, x, y)
        self.side = side
        
class Circle(Shape):
    """Circle Class: inherits from Shape and has method area"""
    def __init__(self, r=1, x=0, y=0):
        Shape.__init__(self, x, y)
        self.radius = r
    def area(self):
        """Area of a Cirle is pi multipled by square of radius"""
        return math.pi * math.pow(self.radius, 2) 
    def __str__(self):
        return "Circle of radius {0} at coordinates ({1}, {2})".\
        format(self.radius, self.x, self.y)