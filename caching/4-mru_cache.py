"""Module for learning about fifo cache
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Class for LRY Caching
    """
    def __init__(self):
        """ Initialize and change order to LIFO
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add item to cache, remove oldest if its full
        """
        if key is None:
            return None
        if item is None:
            return None
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                discard = self.order.pop()
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))

        if key in self.cache_data:
            self.order.remove(key)

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Return item from cache, update order
        """
        if key is None:
            return None
        if key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data.get(key)
