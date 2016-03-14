#!/usr/bin/env python
import json

ADMIN_USER = 'admin'
ADMIN_PWD = 'admin'
import time
from collections import defaultdict

class Db(defaultdict):
    def __init__(self):
        print("Initializing database.")
        super(Db, self).__init__()
        self[ADMIN_USER] = ADMIN_PWD

    def __setitem__(self, key, value):
        'Override the __setitem__ method to insert timestamp.'
        value = (value, time.time())
        super(Db, self).__setitem__(key, value)

    def dumpusers(self):
        for user, (passw, login_ts) in self.items():
            print("{}:{}:{}".format(user, passw, login_ts))

    def newuser(self):
        prompt = 'login desired: '
        while True:
            name = raw_input(prompt)
            if name in self:
                prompt = 'name taken, try another: '
                continue
            else:
                break
        pwd = raw_input('passwd: ')
        self[name] = pwd

    def olduser(self):
        name = raw_input('login: ')
        pwd = raw_input('passwd: ')
        passwd = self.get(name)[0]
        if passwd == pwd:
            pass
            print ("You last logged in: {}".format(self.get(name)[1]))
        if name == ADMIN_USER:
            self.dumpusers()
        else:
            print 'login incorrect'
            return

        print 'welcome back', name

    def showmenu(self):
        prompt = """
    (N)ew User Login
    (E)xisting User Login
    (Q)uit

    Enter choice: """

        done = 0
        while not done:
            chosen = 0
            while not chosen:
                try:
                    choice = raw_input(prompt)[0]
                except (EOFError, KeyboardInterrupt):
                    choice = 'q'
                print '\nYou picked: [%s]' % choice

                if choice not in 'neq':
                    print 'invalid menu option, try again'
                else:
                    chosen = 1

            if choice == 'q':
                done = 1
            if choice == 'n':
                self.newuser()
            if choice == 'e':
                self.olduser()

if __name__ == '__main__':
    my_db = Db()
    my_db.showmenu()