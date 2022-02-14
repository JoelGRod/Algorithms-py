import unittest
from algorithms.main.maths.prime_factors import prime_factors

class TestPrimeFactors(unittest.TestCase):
    def test_prime_factors(self):
        self.assertEqual(prime_factors(12), [2, 2, 3])
        self.assertEqual(prime_factors(13), [13])


if __name__ == '__main__':
    unittest.main()