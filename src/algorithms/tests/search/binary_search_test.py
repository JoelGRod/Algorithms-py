import unittest
from algorithms.main.search.binary_search import binary_search_recursive as bsr, binary_search as bs

class TestBreadFirstSearch(unittest.TestCase):
    def setUp(self):
        self.numbers = [1, 3, 4, 6, 7, 9, 12,
                        14, 16, 18, 20, 24, 28, 36, 45, 56]
        self.value = 56
        self.wrong_value = 234

    def test_binary_search_success(self):
        expected = 15
        self.assertEqual(bs(self.numbers, self.value), expected)

    def test_binary_search_fail(self):
        expected = None
        self.assertEqual(bs(self.numbers, self.wrong_value), expected)

    def test_binary_search_recursive_success(self):
        expected = True
        self.assertEqual(bsr(self.numbers, self.value), expected)

    def test_binary_search_recursive_fail(self):
        expected = False
        self.assertEqual(bsr(self.numbers, self.wrong_value), expected)


if __name__ == '__main__':
    unittest.main()
