#!/usr/bin/env python3


class Point(object):
    def __init__(self, x=0, y=0):
        'Point initializer, set non-specified values to origin.'
        self.x = x
        self.y = y

    def __str__(self):
        return "x:{} y:{}".format(self.x, self.y)

    __repr_ = __str__


class Line(object):
    def __init__(self, point_a, point_b):
        'Line initializer, set point values to be '
        if isinstance(point_a, tuple):
            point_a_x, point_a_y = point_a
            self.point_a = Point(point_a_x, point_a_y)
        elif isinstance(point_a, Point):
            self.point_a = point_a
        if isinstance(point_b, tuple):
            point_b_x, point_b_y = point_b
            self.point_b = Point(point_b_x, point_b_y)
        elif isinstance(point_b, Point):
            self.point_b = point_b

    def __str__(self):
        return "A:{}\nB:{}".format(self.point_a, self.point_b)

    __repr__ = __str__

    @property
    def length(self):
        return ((self.point_a.x - self.point_b.x) + (self.point_b.y - self.point_b.y))**2

    @property
    def slope(self):
        try:
            return (self.point_b.y - self.point_a.y)/(self.point_b.x - self.point_a.x)
        except (ZeroDivisionError, ValueError):
            return None