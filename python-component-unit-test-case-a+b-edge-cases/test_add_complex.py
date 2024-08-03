import unittest
from decimal import Decimal

def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_addition_large_numbers(self):
        # Overflow test
        self.assertEqual(add(1e308, 1e308), float('inf'))
        # Underflow test
        self.assertAlmostEqual(add(1e-308,1e-308), 0.0, places = 10)
    
    def test_addition_float_precision(self):
        # Floating-point precision

        actual_result = add(0.2, 0.1)
        expected_result = 0.3

        self.assertAlmostEqual(actual_result, expected_result, places = 1)

    def test_addition_complex_numbers(self):
        self.assertEqual(add(complex(2,3), complex(4,-1)), complex(6,2))
    
    def test_addition_invalid_input(self):
        with self.assertRaises(TypeError):
            add("five", 5)