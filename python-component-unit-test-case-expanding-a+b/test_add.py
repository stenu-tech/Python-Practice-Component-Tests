import unittest

def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_addition_positive_integers(self):
        self.assertEqual(add(2,3), 5)
    def test_addition_negative_integers(self):
        self.assertEqual(add(-2,-3), -5)
    def test_addition_zero_values(self):
        self.assertEqual(add(0,0), 0)
        self.assertEqual(add(5,0), 5)
        self.assertEqual(add(0,-5), -5)
    def test_addition_float_values(self):
        self.assertEqual(add(2.3,2.7), 5)
        self.assertEqual(add(4.0,1), 5)
    def test_invalid_values(self):
        with self.assertRaises(TypeError):
            add("Hello World", 5)