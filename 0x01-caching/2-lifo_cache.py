#!/usr/bin/env python3
""" a class BasicCache that inherits from
    BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ a subclass of BaseCaching"""

    def __init__(self):
        """ intialize from parent class"""
        self.lifo = []
        BaseCaching.__init__(self)
        # super(BasicCache, self).__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            # print(type(self.cache_data))
            pass
        else:
            # print(type(self.cache_data))
            self.lifo.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > super().MAX_ITEMS:
                discard_key = self.lifo.pop(-2)
                del self.cache_data[discard_key]
                print(f'DISCARD: {discard_key}')

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
