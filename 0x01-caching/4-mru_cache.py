#!/usr/bin/env python3
""" 4-mru_cache Module """

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache Class

    Implements the MRU (Most Recently Used) caching algorithm
    """

    def __init__(self):
        """ Initialize the MRUCache object """

        super().__init__()
        self.mru_queue = []

    def _update_queue(self, key):
        """
        Update the MRU queue based on the provided key.

        Args:
            key: The key of the item.
        """

        if key in self.mru_queue:
            self.mru_queue.remove(key)
        self.mru_queue.insert(0, key)

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

        self.cache_data[key] = item
        self._update_queue(key)

        if len(self.cache_data) > self.MAX_ITEMS:
            discarded_key = self.mru_queue.pop()
            del self.cache_data[discarded_key]
            print("DISCARD: {}".format(discarded_key))

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

        self._update_queue(key)
        return self.cache_data[key]

        
