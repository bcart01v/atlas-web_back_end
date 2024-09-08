#!/usr/bin/python3
"""Module for learning about fifo cache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Class for LIFO Caching
    """
    def __init__(self):
        """ Initialize and change order to LIFO
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add item to cache (If it exists)
        """
        if key is None:
            return
        if item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                discard = self.order.pop()
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ return item from Cache (If it exists)
        """
        if key is None:
            return None
        if key not in self.cache_data:
            return None
        return self.cache_data.get(key)
