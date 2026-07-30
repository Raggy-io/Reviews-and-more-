import unittest
from review_generator.engine import hash_seed, LCG

class TestEngine(unittest.TestCase):
    def test_hash_seed_consistency(self):
        """Test that the same seed string always produces the same hash."""
        seed1 = hash_seed("product_123")
        seed2 = hash_seed("product_123")
        self.assertEqual(seed1, seed2)
        
        # Test different strings produce different hashes (usually)
        seed3 = hash_seed("product_124")
        self.assertNotEqual(seed1, seed3)

    def test_lcg_consistency(self):
        """Test that LCG produces the same sequence given the same seed."""
        lcg1 = LCG(12345)
        seq1 = [lcg1.next_float() for _ in range(10)]
        
        lcg2 = LCG(12345)
        seq2 = [lcg2.next_float() for _ in range(10)]
        
        self.assertEqual(seq1, seq2)

    def test_lcg_bounds(self):
        """Test that next_float() stays within [0, 1)."""
        lcg = LCG(9999)
        for _ in range(100):
            val = lcg.next_float()
            self.assertTrue(0.0 <= val < 1.0)

    def test_lcg_pick(self):
        """Test picking items from a list."""
        lcg = LCG(42)
        items = ["A", "B", "C", "D"]
        
        # Picking should be deterministic
        picked = lcg.pick(items)
        self.assertIn(picked, items)
        
        # Should return None for empty lists
        self.assertIsNone(lcg.pick([]))

if __name__ == "__main__":
    unittest.main()
