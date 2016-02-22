#!/usr/bin/env python3
import os

class ConfigDict(dict):

    def __init__(self, config_file):
        #super(ConfigDict, self).__init__(self)
        if os.path.exists(config_file):
            self.config_file = config_file
            with open(self.config_file, 'r') as fh:
                # http://bit.ly/1oWKAxc
                all_lines = (line.rstrip() for line in fh)
                non_blank_lines = (line for line in all_lines if line)
                for line in non_blank_lines:
                    line = line.strip()
                    (key, value) = line.split("=", 1)
                    #print("{}:{}".format(key, value))
                    self.__setitem__(key, value)
            self.write_dict_to_file()
        else:
            print("Import failed due to file {} not existing".format(config_file))

    def __setitem__(self, key, value):
        #print("key:{}  value:{}".format(key, value))
        dict.__setitem__(self, key, value)
        self.write_dict_to_file()

    def write_dict_to_file(self):
        keys_list = self.keys()
        sorted_keys = sorted(keys_list)
        with open(self.config_file, 'w') as fh:
            for key in sorted_keys:
                fh.write('{}={}\n'.format(key, self[key]))
