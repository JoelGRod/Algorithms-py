import unittest
from algorithms.main.maths.number_divisors import divisors

class TestDivisors(unittest.TestCase):
    def test_number_divisors(self):
        self.assertEqual(divisors(15), [3,5])
        self.assertEqual(divisors(253), [11,23])
        self.assertEqual(divisors(24), [2,3,4,6,8,12])
        self.assertEqual(divisors(25), [5])
        self.assertEqual(divisors(13), "13 is prime")
        self.assertEqual(divisors(3), "3 is prime")
        self.assertEqual(divisors(29), "29 is prime")


if __name__ == '__main__':
    unittest.main()