#!/usr/bin/env python3
""" 100-lfu_cache Module """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache Class

    Implements the LFU (Least Frequently Used) algorithm
    """

    def __init__(self):
        """ Initialize the LFUCache instance """

        super().__init__()
        self.frequency = {}
        self.frequency_queue = [[] for _ in range(self.MAX_ITEMS + 1)]

    def _update_frequency(self, key):
        """
        Update the frequency count of the provided key.

        Args:
            key: The key of the item.

        Return:
            Increments frequency count of key by 1 and moves the key
            to the corresponding frequency queue.
            Add 1 If the key doesn't exist
        """
        if key in self.frequency:
            current_count = self.frequency[key]
            self.frequency[key] += 1
            self.frequency_queue[current_count].remove(key)
        else:
            self.frequency[key] = 1

        self.frequency_queue[self.frequency[key]].append(key)

    def _evict(self):
        """
        Evict the least frequently used items from the cache.
        """
        for queue in self.frequency_queue:
            if len(queue) > 0:
                discarded_key = queue.pop(0)
                del self.cache_data[discarded_key]
                del self.frequency[discarded_key]
                print("DISCARD: {}".format(discarded_key))
                break

    def put(self, key, item):
        """
        Add an item to the cache

        Args:
            key: The key for the item.
            item: The value of the item.

        Return:
            Nothing, If the key or item is None,
            Otherwise, assigns item to key in cache_data dictionary.
        """

        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self._update_frequency(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                self._evict()
            self.cache_data[key] = item
            self._update_frequency(key)

    def get(self, key):
        """
        Get an item from the cache

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value of key in the cache_data dictionary,
            or None if key is None or does not exist
        """

        if key is None or key not in self.cache_data:
            return None

        self._update_frequency(key)
        return self.cache_data[key]
