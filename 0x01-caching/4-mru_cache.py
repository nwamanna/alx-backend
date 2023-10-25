#!/usr/bin/env python3
""" a class BasicCache that inherits from
    BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ a subclass of BaseCaching"""

    def __init__(self):
        """ intialize from parent class"""
        self.lifo = []
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
                self.lifo.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > super().MAX_ITEMS:
                max_val = max(self.count.values())
                print(max_val)
                max_list = [key for key, value in self.count.items()
                            if value == max_val]
                if len(max_list) > 1:
                    print(max_list)
                    print(f'count dict: {self.count}')
                    discard_key = self.lifo.pop(-2)
                    del self.cache_data[discard_key]
                    del self.count[discard_key]
                    print(f'DISCARD: {discard_key}')

                else:
                    print(f'count dict: {self.count}')
                    del self.cache_data[max_list[0]]
                    del self.count[max_list[0]]
                    self.lifo.remove(max_list[0])
                    print(f'DISCARD: {max_list[0]}')
                print(f'lifo: {self.lifo}')
                print(f'count dict: {self.count}')
                for k in self.count.keys():
                    self.count[k] = 0

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
