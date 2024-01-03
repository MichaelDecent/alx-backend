#!/usr/bin/python3
"""
This Module contain a class FIFO Cache that inherites from BaseCaching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO Cache Algorithm
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key = list(self.cache_data.keys())[0] 
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
