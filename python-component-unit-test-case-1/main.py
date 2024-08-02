import unittest

""" Test case of unit tests of adding up sum of mixed integer and floating numbers of a and b
"""

class TestCalculate(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(aplusb(), 20)
    
    def test_floating_numbers(self):
        self.assertEqual(aplusb(10.5, 10.5), 21)

    def test_negative_integers(self):
        self.assertEqual(aplusb(-10.5, -10.5), -21)


def aplusb(a = 10, b = 10):
    return a + b

if __name__ == "__main__":
    unittest.main()