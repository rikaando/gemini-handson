import unittest

from main import hello_world

class TestHelloWorld(unittest.TestCase):

    def test_hello_world_returns_correct_message(self):
        expected_response = {"message": "Hello, World!"}
        actual_response = hello_world()
        self.assertEqual(actual_response, expected_response)

if __name__ == '__main__':
    unittest.main()
