import unittest
from algorithms.main.strings.sort_strings_by_number import order

class TestSortStringByNumber(unittest.TestCase):
    def test_sort_string_by_number(self):
        self.assertEqual(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
        self.assertEqual(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
        self.assertEqual(order(""), "")
        self.assertEqual(order("is2 This1 Test4 a3"), "This1 is2 a3 Test4")
        self.assertEqual(order("something1 something12 something17 something2"), "something1 something2 something12 something17")



if __name__ == '__main__':
    unittest.main()