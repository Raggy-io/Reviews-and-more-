import unittest
from fastapi.testclient import TestClient
from api.main import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_read_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

    def test_get_reviews(self):
        """Test getting reviews and checking cache hits."""
        # First request (cache miss)
        response1 = self.client.get("/reviews/prod_123?count=3")
        self.assertEqual(response1.status_code, 200)
        data1 = response1.json()
        self.assertEqual(data1["source"], "generator")
        self.assertEqual(data1["count"], 3)
        self.assertEqual(len(data1["reviews"]), 3)

        # Second request (cache hit)
        response2 = self.client.get("/reviews/prod_123?count=3")
        self.assertEqual(response2.status_code, 200)
        data2 = response2.json()
        self.assertEqual(data2["source"], "cache")
        # Ensure data is identical
        self.assertEqual(data1["reviews"], data2["reviews"])

    def test_get_reviews_validation(self):
        """Test query parameter validation (count must be <= 20)."""
        response = self.client.get("/reviews/prod_123?count=50")
        self.assertEqual(response.status_code, 422) # Unprocessable Entity

    def test_cache_stats(self):
        self.client.get("/reviews/cache_test_1")
        response = self.client.get("/system/cache/stats")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("capacity", data)
        self.assertIn("current_size", data)
        self.assertGreaterEqual(data["current_size"], 1)

if __name__ == '__main__':
    unittest.main()
