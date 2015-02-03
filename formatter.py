#!/usr/bin/env python3
# encoding: utf-8
"""
formatter.py

Created by Terry Bates on 2015-02-02.
Copyright (c) 2015 http://the-awesome-python-blog.posterous.com. All rights
reserved.
"""


def format_string(string, formatter=None):
    '''Format a string using the formatter object, which
    is expected to have a format() method that accepts
    a string.'''
    class DefaultFormatter:
        '''Format a string in title case.'''
        def format(self, string):
            '''By default format string based on title case.'''
            return str(string).title()
    if not formatter:
        formatter = DefaultFormatter()
    return formatter.format(string)


def main():
    '''Main function.'''
    hello_string = "hello world, how are you today?"
    print(" input: " + hello_string)
    print("output: " + format_string(hello_string))


if __name__ == '__main__':
    main()
