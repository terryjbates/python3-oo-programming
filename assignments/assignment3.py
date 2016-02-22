#!/usr/bin/env python3


class ConfigDict(dict):

    def __init__(self, config_file):
        #super(ConfigDict, self).__init__(self)
        self.config_file = config_file
        try:
            with open(self.config_file, 'r') as fh:
                all_lines = (line.rstrip() for line in fh)
                non_blank_lines = (line for line in all_lines if line)
                for line in non_blank_lines:
                    line = line.strip()
                    (key, value) = line.split("=")
                    print("{}:{}".format(key, value))
                    self.__setitem__(key, value)
            self.write_dict_to_file()
        except Exception as ex:
            print("Import failed due to: {}".format(ex))

    def __setitem__(self, key, value):
        print("key:{}  value:{}".format(key, value))
        dict.__setitem__(self, key, value)
        self.write_dict_to_file()


    def write_dict_to_file(self):
        keys_list = self.keys()
        sorted_keys = sorted(keys_list)
        with open(self.config_file, 'w') as fh:
            for key in sorted_keys:
                fh.write('{}={}\n'.format(key, self[key]))
