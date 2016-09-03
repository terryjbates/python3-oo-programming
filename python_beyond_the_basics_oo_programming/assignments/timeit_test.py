#!/usr/bin/env python

import timeit

my_dict = {'a': 5, 'b': 6, 'c': 7}
number = 1000000

#print(timeit.timeit('math.sqrt(2.0)', 'import math'))

print (timeit.timeit("my_dict['c']", "my_dict = {'a': 5, 'b': 6, 'c': 7}", number=1000000))

print (timeit.timeit("my_dict.get('c')", "my_dict = {'a': 5, 'b': 6, 'c': 7}", number=1000000))