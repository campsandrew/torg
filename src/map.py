import os
import sys

class Map(dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    self[k] = v

        if kwargs:
            for k, v in kwargs.items():
                self[k] = v

        return None

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super().__delitem__(key)
        del self.__dict__[key]

    @staticmethod
    def recursive_map(mp):
        nomap = []

        for attr in [a for a in vars(mp)]:
            if attr in nomap: continue
            if type(mp[attr]) is not dict:
                if type(mp[attr]) is list:
                    for i, item in enumerate(mp[attr]):
                        if type(item) is dict:
                            mp[attr][i] = Map.recursive_map(Map(item))
                continue

            mp[attr] = Map.recursive_map(Map(mp[attr]))

        return mp