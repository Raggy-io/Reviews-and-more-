import unittest
from review_generator.cache import LRUCache

class TestLRUCache(unittest.TestCase):
    def test_cache_capacity_and_eviction(self):
        """Test that the cache correctly evicts the least recently used item."""
        cache = LRUCache(capacity=2)
        
        cache.put("A", 1)
        cache.put("B", 2)
        
        self.assertEqual(cache.get("A"), 1)
        self.assertEqual(cache.get("B"), 2)
        
        # Adding C should evict A, because B was accessed more recently (in the line above)
        cache.put("C", 3)
        
        self.assertIsNone(cache.get("A"))
        self.assertEqual(cache.get("B"), 2)
        self.assertEqual(cache.get("C"), 3)

    def test_cache_update_existing(self):
        """Test that updating an existing key moves it to the most recently used position."""
        cache = LRUCache(capacity=2)
        
        cache.put("A", 1)
        cache.put("B", 2)
        
        # Update A
        cache.put("A", 99)
        
        # Adding C should evict B, because A was just updated
        cache.put("C", 3)
        
        self.assertEqual(cache.get("A"), 99)
        self.assertIsNone(cache.get("B"))
        self.assertEqual(cache.get("C"), 3)

    def test_invalid_capacity(self):
        """Test that initializing with invalid capacity raises an error."""
        with self.assertRaises(ValueError):
            LRUCache(capacity=0)
        with self.assertRaises(ValueError):
            LRUCache(capacity=-5)

if __name__ == '__main__':
    unittest.main()
