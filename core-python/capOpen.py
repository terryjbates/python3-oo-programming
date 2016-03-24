#!/usr/bin/env python3


class CapOpen(object):
    def __init__(self, fn, mode='r', buf=-1):
        self.file = open(fn, mode, buf)

    def __str__(self):
        return str(self.file)

    def __repr__(self):
        return 'self.file'

    def write(self, line):
        self.file.write(line.upper())

    def writelines(self, line_list, newline=False):
        cr = ''
        if newline:
            cr = '\n'
        for line in line_list:
            self.write(line + cr)

    def __getattr__(self, attr):
        return getattr(self.file, attr)