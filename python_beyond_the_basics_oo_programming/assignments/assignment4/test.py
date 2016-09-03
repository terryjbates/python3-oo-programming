#!/usr/bin/python

"""
    Usages:
    ./test.py                    (reads out the entire config dict)
    ./test.py thiskey thisvalue  (sets 'thiskey' and 'thisvalue' in the dict)
"""
import sys
from assignment3 import ConfigDict      # assumes "assignment3.py" holds a
                                        # class caleld ConfigDict

cd = ConfigDict('./config_file.txt')

# if 2 arguments on the command line,
# set a key and value in the object's dictionary
if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    print('writing data:  {0}, {1}'.format(key, value))
    cd[key] = value

# if 1 argument on the command line, treat it as a key and show the value
elif len(sys.argv) == 2:
    print('reading a value')
    key = sys.argv[1]
    print('the value for {0} is {1}'.format(sys.argv[1], cd[key]))

# if no arguments on the command line, show all keys and values
else:
    print('keys/values:')
    for key in cd.keys():
        print('   {0} = {1}'.format(key, cd[key]))