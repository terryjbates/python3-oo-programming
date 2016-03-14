#!/usr/bin/env python3

ADMIN_USER = 'admin'
ADMIN_PWD = 'admin'
import time
from collections import defaultdict
import json


class Db(defaultdict):
    def __init__(self, db_file=None):
        if db_file:
            try:
                print("Attempting to load {}".format(db_file))
                with open(db_file) as fd:
                    file_data = dict(json.load(fd))
                    for key, val in list(file_data.items()):
                        self[key] = val
                self.db_file = db_file
            except IOError as open_ex:
                print("Unable to open file due to: {}".format(open_ex))
                print("Creating {} as file".format(db_file))
                self.db_file = db_file
        else:
            self.db_file = 'default.db'
            print("Initializing database.")
            super(Db, self).__init__()
            self[ADMIN_USER] = ADMIN_PWD

    def write_to_file(func):
        def wrapped(self=None):
            # print("Wrapped shit! Using {}".format(self.db_file))
            func(self)
            with open(self.db_file, 'w') as fd:
                dump_dict = {key: val for key, val in list(self.items())}
                json.dump(dump_dict, fd)

        return wrapped


    def __setitem__(self, key, value):
        """Override the __setitem__ method to insert timestamp."""
        value = (value, time.time())
        super(Db, self).__setitem__(key, value)

    def dumpusers(self):
        for user, (passw, login_ts) in list(self.items()):
            print("{}:{}:{}".format(user, passw, login_ts))

    @write_to_file
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

    @write_to_file
    def olduser(self):
        name = raw_input('login: ')
        pwd = raw_input('passwd: ')
        passwd = self.get(name)[0]
        if passwd == pwd:
            pass
            print("You last logged in: {}".format(self.get(name)[1]))
        if name == ADMIN_USER:
            self.dumpusers()
        else:
            print('login incorrect')
            return

        print('welcome back', name)

    def showmenu(self):
        choice = None
        prompt = """
    (N)ew User Login
    (E)xisting User Login
    (Q)uit

    Enter choice: """
        while choice != 'q':
            choice = raw_input(prompt)
            choice = choice.lower()
            print ("Choice after lowering :", choice)

            if choice not in 'neq':
                print ('invalid menu option, try again')

            if choice == 'q':
                print ("Exiting...")
            if choice == 'n':
                self.newuser()
            if choice == 'e':
                self.olduser()


if __name__ == '__main__':
    my_db = Db()
    my_db.showmenu()
