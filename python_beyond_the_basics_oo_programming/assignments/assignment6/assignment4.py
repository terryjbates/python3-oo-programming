#!/usr/bin/env python3
import os


class ConfigKeyError(Exception):
    def __init__(self, this, key):
        self.key = key
        self.keys = this.keys()

    def __str__(self):
        return "key '{}' not found. Available keys: {}.".format(self.key, ' '.join(self.keys))


class ConfigDict(dict):

    def __init__(self, config_file):
        #super(ConfigDict, self).__init__(self)
        self._filename = config_file
        if os.path.exists(config_file) and os.access(config_file, os.R_OK):
            with open(self._filename, 'r') as fh:
                # http://bit.ly/1oWKAxc
                all_lines = (line.rstrip() for line in fh)
                non_blank_lines = (line for line in all_lines if line)
                for line in non_blank_lines:
                    line = line.strip()
                    (key, value) = line.split("=", 1)
                    #print("{}:{}".format(key, value))
                    self.__setitem__(key, value)
        else:
            open(self._filename, 'a').close()
            self.update({})
        self.write_dict_to_file()
    def __setitem__(self, key, value):
        #print("key:{}  value:{}".format(key, value))
        dict.__setitem__(self, key, value)
        self.write_dict_to_file()

    def write_dict_to_file(self):
        keys_list = self.keys()
        sorted_keys = sorted(keys_list)
        with open(self._filename, 'w') as fh:
            for key in sorted_keys:
                fh.write('{}={}\n'.format(key, self[key]))

    def __getitem__(self, key):
        if not key in self:
            raise ConfigKeyError(self, key)
        return dict.__getitem__(self, key)




#cd = ConfigDict('/tmp/somefile.txt')

#print cd['nonexistent_key']