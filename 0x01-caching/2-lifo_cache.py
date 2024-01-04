#!/usr/bin/python3
"""
This Module contain a class LIFO Cache that inherites from BaseCaching
"""
from base_caching import BaseCaching
from collections import deque


class LIFOCache(BaseCaching):
    """
    LIFO Cache Algorithm
    """

    def __init__(self):
        super().__init__()
        self.keys = deque()

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            if key in self.cache_data:
                self.keys.remove(key)
                self.keys.append(key)
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = self.keys.pop()
                self.cache_data.pop(last_key)
                print(f"DISCARD: {last_key}")

            self.keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
