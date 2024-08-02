import unittest

""" A demonstration of a simple addition component unit test.
"""

def calculate(A = 15, B = 15):
    """ return an addition of A and B which are passed to the function scope. """
    return A + B

class TestCalculate(unittest.TestCase):

    def test_default_values(self):
        # Test Case 1: Default Values
        self.assertEqual(calculate(), 30, "Test failed for default values (15, 15)")

    def test_positive_integers(self):
        # Test case 2: Positive integers (Equivalence Class: Positive integers)
        self.assertEqual(calculate(10, 20), 30, "Failed on positive integers (10, 20)")

    def test_negative_integers(self):
        # Test case 3: Negative integers (Equivalence Class: Negative integers)
        self.assertEqual(calculate(-10, -20), -30, "Failed on negative integers (-10, -20)")

    def test_mixed_integers(self):
        # Test case 4: Mixed integers (Equivalence Class: Mixed integers)
        self.assertEqual(calculate(10, -20), -10, "Failed on mixed integers (10, -20)")

    def test_zero_values(self):
        # Test case 5: Zero values (Equivalence Class: Zero values)
        self.assertEqual(calculate(0, 0), 0, "Failed on zero values (0, 0)")


if __name__ == "__main__":
    unittest.main()
