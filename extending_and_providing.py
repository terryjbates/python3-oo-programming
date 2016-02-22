#!/usr/bin/python 2

import random
import StringIO

class WriteMyStuff(object):

    def __init__(self, writer):
        self.writer = writer

    def write(self):
        write_text = "A silly Message"
        self.writer.write(write_text)

with open('test.txt', 'w') as out_file:
    w1 = WriteMyStuff(out_file)
    w1.write()

sioh = StringIO.StringIO()
w2 = WriteMyStuff(sioh)
w2.write()

print('fie object', open('test.txt', 'r').read())
print('StringIO object: {}'.format(sioh.getvalue()))
