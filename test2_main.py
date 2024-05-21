import unittest
import json

from main import app

class TestHello(unittest.TestCase):

    def test_hello(self):
        client = app.test_client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"message": "Hello, World!"})

if __name__ == "__main__":
    unittest.main()
