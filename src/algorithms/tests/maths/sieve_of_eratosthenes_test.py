import unittest
from algorithms.main.maths.sieve_of_eratosthenes import sieve_of_eratosthenes

class TestSieveOfEratosthenes(unittest.TestCase):
    def test_sieve_of_eratosthenes(self):
        self.assertEqual(sieve_of_eratosthenes(12), [2, 3, 5, 7, 11])
        self.assertEqual(sieve_of_eratosthenes(13), [2, 3, 5, 7, 11, 13])


if __name__ == '__main__':
    unittest.main()