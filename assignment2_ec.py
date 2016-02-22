#!/usr/bin/env python
import datetime
import abc


class WriteFile(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, filename):
        try:
            self.fh = open(filename, 'a')
        except TypeError:
            print("Invalid file specified.")

    @abc.abstractmethod
    def write(self, input_str):
        return


class LogFile(WriteFile):

    def write(self, input_str):
        self.fh.write(input_str)


class DelimFile(WriteFile):

    def __init__(self, filename, delim):
        super(DelimFile, self).__init__(filename)
        self.delim = delim

    def write(self, input_str):
        delim_str = self.delim.join(input_str)
        self.fh.write(self.timestamp() + '\t' + delim_str)

    @staticmethod
    def timestamp():
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M')


test = LogFile('/tmp/mytest.txt')
test.write('foobar')

test_list = ['a', 'b', 'c', 'd', 'e', 'f']
c = DelimFile('/tmp/text.csv', ',')

c.write(test_list)
