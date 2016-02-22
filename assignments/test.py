#!/usr/bin/env python3

import sys

from assignment3 import ConfigDict

cd = ConfigDict('config_file.txt')

if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    print('Writing data: {}, {}'.format(key, value))

    cd[key] = value

else:
    print('reading data')
    for key in cd.keys():
        print('    {} = {}'.format(key, cd[key]))
