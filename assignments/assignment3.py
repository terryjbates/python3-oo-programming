#!/usr/bin/env python3


class ConfigDict(dict):

    def __init__(self, config_file):
        super(ConfigDict, self).__init__(self)
        try:
            with open(config_file, 'r') as fh:
                for line in fh:
                    (key, value) = line.split("=")
                    print("{}:{}".format(key, value))
                    self.__setitem__(key, value)
        except Exception as ex:
            print("Import failed due to {}".format(ex))


    def __setitem__(self, key, value):
        print("key:{}  value:{}".format(key, value))
        dict.__setitem__(self, key, value)

