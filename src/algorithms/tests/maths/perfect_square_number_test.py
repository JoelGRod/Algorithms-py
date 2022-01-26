import unittest
from algorithms.main.maths.perfect_square_number import is_square

class IsSquareNumber(unittest.TestCase):
    def test_is_square(self):
        self.assertEqual(is_square(-1), False)
        self.assertEqual(is_square(0), True)
        self.assertEqual(is_square(3), False)
        self.assertEqual(is_square(4), True)
        self.assertEqual(is_square(25), True)
        self.assertEqual(is_square(26), False)


if __name__ == '__main__':
    unittest.main()
