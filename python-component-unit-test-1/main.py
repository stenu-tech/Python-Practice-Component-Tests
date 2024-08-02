import unittest

def greet():
    return 'Hello World!'

class TestUser(unittest.TestCase):
    def test_greet_output(self):
        greet_output = greet()
        self.assertEqual(greet_output, 'Hello World!')