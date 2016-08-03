#!/usr/bin/env python2

import threading
from time import ctime


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        super().__init__()
        self.name = name
        self.func = func
        self.args = args
        self.result = ''

    def run(self):
        print("starting {} at {}".format(self.name, ctime()))
        self.result = self.func(*self.args)
        print("{} finished at {}".format(self.name, ctime()))

    def getResult(self):
        return self.result
