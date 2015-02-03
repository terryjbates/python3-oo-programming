#!/usr/bin/env python3
# encoding: utf-8
"""
point.py

Created by Terry Bates on 2015-01-31.
Copyright (c) 2015 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import math

class Point:
    'Represents a point in two-dimensional geometric coordinates'
    def __init__(self, x, y):
        '''Initialize the position of a new point. The x and y
           coordinates can be specified. If they are not, the point
           defaults to the origin.'''
        self.move(x, y)
        
    def move(self, x, y):
        "Move the point to a new location in two-dimensional space."
        self.x = x
        self.y = y
        
    def reset(self):
        'Reset the point back to the geometric origin: 0, 0'
        self.move(0, 0)
        
    def calculate_distance(self, other_point):
        """Calculate the distance from this point to a second point
        passed as a parameter.
        This function uses the Pythagorean Theorem to calculate
        the distance between the two points. The distance is returned
        as a float."""
        return math.sqrt(
            (self.x - other_point.x)**2 +
            (self.y - other_point.y)**2)


point1 = Point(0,0)
point2 = Point(1,2)

point1.reset()
point2.move(5, 0)

print(point2.calculate_distance(point1))
assert (point2.calculate_distance(point1) == point1.calculate_distance(point2))
point1.move(3,4)
print(point1.calculate_distance(point2))
print(point1.calculate_distance(point1))
