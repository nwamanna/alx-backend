#!/usr/bin/env python3
""" a class BasicCache that inherits from
    BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ a subclass of BaseCaching"""

    def __init__(self):
        """ intialize from parent class"""
        self.fifo = []
        self.count = {}
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
            if key in self.count:
                self.count[key] += 1
            else:
                self.count[key] = 0
                self.fifo.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > super().MAX_ITEMS:
                min_val = min(self.count.values())
                print(min_val)
                min_list = [key for key, value in self.count.items()
                            if value == min_val]
                if len(min_list) > 1:
                    print(min_list)
                    discard_key = self.fifo.pop(0)
                    del self.cache_data[discard_key]
                    del self.count[discard_key]
                    print(f'DISCARD: {discard_key}')
                else:
                    del self.cache_data[min_list[0]]
                    del self.count[min_list[0]]
                    self.fifo.remove(min_list[0])
                    print(f'DISCARD: {min_list[0]}')
                print(f'fifo: {self.fifo}')
                print(f'count dict: {self.count}')

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        if key in self.count:
            self.count[key] += 1
        else:
            self.count[key] = 0
        return self.cache_data[key]
