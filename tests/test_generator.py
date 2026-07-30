import unittest
from review_generator import ReviewGenerator

class TestGenerator(unittest.TestCase):
    def test_deterministic_generation(self):
        """Test that the same product ID always generates the exact same reviews."""
        product_id = "test_product_99"
        
        reviews_1 = ReviewGenerator.generate(product_id, count=5)
        reviews_2 = ReviewGenerator.generate(product_id, count=5)
        
        self.assertEqual(len(reviews_1), 5)
        self.assertEqual(len(reviews_2), 5)
        
        for r1, r2 in zip(reviews_1, reviews_2):
            self.assertEqual(r1.id, r2.id)
            self.assertEqual(r1.author, r2.author)
            self.assertEqual(r1.rating, r2.rating)
            self.assertEqual(r1.title, r2.title)
            self.assertEqual(r1.body, r2.body)

    def test_different_products_differ(self):
        """Test that different product IDs generate different reviews (usually)."""
        r1 = ReviewGenerator.generate("prod_A", count=1)[0]
        r2 = ReviewGenerator.generate("prod_B", count=1)[0]
        
        self.assertNotEqual(r1.id, r2.id)
        # It's highly probable author, title, or body will differ.
        self.assertTrue(r1.author != r2.author or r1.title != r2.title or r1.body != r2.body)

    def test_empty_product_id(self):
        """Test handling of empty product IDs."""
        reviews = ReviewGenerator.generate("", count=4)
        self.assertEqual(reviews, [])
        self.assertEqual(ReviewGenerator.generate(None, count=4), [])

    def test_average_rating(self):
        """Test average rating calculation."""
        reviews = ReviewGenerator.generate("test", count=3)
        # Manually force some ratings for the test
        reviews[0].rating = 5
        reviews[1].rating = 4
        reviews[2].rating = 4
        
        avg = ReviewGenerator.average_rating(reviews)
        self.assertEqual(avg, round(13 / 3, 1))

    def test_average_rating_empty(self):
        """Test average rating for empty list."""
        self.assertEqual(ReviewGenerator.average_rating([]), 4.5)

if __name__ == "__main__":
    unittest.main()
