#!/usr/bin/env python3
import os
import cPickle

class ConfigKeyError(Exception):
    def __init__(self, this, key):
        self.key = key
        self.keys = this.keys()

    def __str__(self):
        return "key '{}' not found. Available keys: {}.".format(self.key, ' '.join(self.keys))


class ConfigPickleDict(dict):
    config_directory = './configs/'

    def __init__(self, config_name):
        self._filename = os.path.join(ConfigPickleDict.config_directory, config_name + '.pickle')
        if not os.path.isfile(self._filename):
            with open(self._filename, 'w') as fh:
                cPickle.dump({}, fh)
        with open(self._filename) as fh:
            pkl = cPickle.load(fh)
            self.update(pkl)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._filename, 'w') as fh:
            cPickle.dump(self, fh)

    def __getitem__(self, key):
        if not key in self:
            raise ConfigKeyError(self, key)
        return dict.__getitem__(self, key)
