#!/usr/bin/python3
"""
This Module contain a class Basic Cache that inherites from BaseCaching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Cache
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
