import unittest
from algorithms.main.maths.sum_by_prime_factors import sum_for_list

class TestSumByPrimeFactors(unittest.TestCase):
    def test_sum_by_prime_factors(self):
        a = [12, 15]
        self.assertEqual(sum_for_list(a), [[2, 12], [3, 27], [5, 15]])
        a = [15, 21, 24, 30, 45]
        self.assertEqual(sum_for_list(a), [[2, 54], [3, 135], [5, 90], [7, 21]])


if __name__ == '__main__':
    unittest.main()