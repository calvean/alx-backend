# 0x01-caching

This repository contains the implementation of various caching system tasks using different cache replacement algorithms. Each task is implemented as a separate class that inherits from the `BaseCaching` class.

The following caching system tasks are included:

    Basic Cache: implements a basic caching system.
        Implementation: 0-basic_cache.py
        Test file: 0-main.py

    FIFO Cache: Implements a First-In-First-Out (FIFO) cache replacement algorithm. The least recently used item is discarded when the cache is full.
        Implementation: 1-fifo_cache.py
        Test file: 1-main.py

    LIFO Cache: Implements a Last-In-First-Out (LIFO) cache replacement algorithm. The most recently used item is discarded when the cache is full.
        Implementation: 2-lifo_cache.py
        Test file: 2-main.py

    LRU Cache: Implements a Least Recently Used (LRU) cache replacement algorithm. The least recently used item is discarded when the cache is full.
        Implementation: 3-lru_cache.py
        Test file: 3-main.py

    MRU Cache: Implements a Most Recently Used (MRU) cache replacement algorithm. The most recently used item is discarded when the cache is full.
        Implementation: 4-mru_cache.py
        Test file: 4-main.py

    LFU Cache: Implements a Least Frequently Used (LFU) cache replacement algorithm. The least frequently used item is discarded when the cache is full. If multiple items have the same usage frequency, the least recently used item among them is discarded.
        Implementation: 100-lfu_cache.py
        Test file: 100-main.py

## Usage

Each caching class provides the following methods:

- `put(key, item)`: Adds a key/value pair to the cache. If the cache is full, a specific cache replacement algorithm is used to discard an existing item.
- `get(key)`: Retrieves the value associated with the given key from the cache. If the key is not present in the cache, None is returned.

## Examples

Here's an example of how to use the LRU Cache:

```
from lru_cache import LRUCache

# Create an instance of the LRU Cache
cache = LRUCache()

# Add key/value pairs to the cache
cache.put("A", 1)
cache.put("B", 2)
cache.put("C", 3)

# Retrieve values from the cache
value_a = cache.get("A")  # Returns 1
value_b = cache.get("B")  # Returns 2
value_c = cache.get("C")  # Returns 3
value_d = cache.get("D")  # Returns None (key not present)

# Output the current cache contents
cache.print_cache()
```

## Author

Calvin Sharara - [Github](https://github.com/calvean)

## License
Public Domain. No copy write protection. 
