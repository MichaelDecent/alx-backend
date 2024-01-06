#!/usr/bin/env python3
"""This module contains implementation of one of the
caching policie, MRU - Most Recently Used"""
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Class implementation of  LFU caching policy"""

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.key_frequency_dict = {}

    def put(self, key, item):
        """Add item/data to the cache storage"""
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least_frequent_key = min(
                self.key_frequency_dict, key=self.key_frequency_dict.get
            )
            self.key_frequency_dict.pop(least_frequent_key)
            self.cache_data.pop(least_frequent_key)
            print("DISCARD: {}".format(least_frequent_key))

        if key not in self.key_frequency_dict:
            self.key_frequency_dict[key] = 0
        else:
            self.key_frequency_dict[key] += 1

    def get(self, key):
        """Retrieve item from the cache"""
        if key is not None and key in self.cache_data:
            self.key_frequency_dict[key] += 1
        return self.cache_data.get(key, None)
