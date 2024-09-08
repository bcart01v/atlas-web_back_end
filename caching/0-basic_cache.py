#!/usr/bin/python3
"""Module for learning about basic cache
"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """
    BasicCache class
    """

    def put(self, key, item):
        """ Add Item to Cache
        """
        if key or item:
            self.cache_data[key] = item
        else:
            return None

    def get(self, key):
        """ Get Item from Cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)