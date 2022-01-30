import unittest
from algorithms.main.strings.highest_scoring_word import high

class TestHighestScoringWord(unittest.TestCase):
    def test_high_scoring_word(self):
        self.assertEqual(high('man i need a taxi up to ubud'), 'taxi')
        self.assertEqual(high('what time are we climbing up the volcano'), 'volcano')
        self.assertEqual(high('take me to semynak'), 'semynak')
        self.assertEqual(high('aa b'), 'aa')
        self.assertEqual(high('b aa'), 'b')
        self.assertEqual(high('bb d'), 'bb')
        self.assertEqual(high('d bb'), 'd')
        self.assertEqual(high("aaa b"), "aaa")


if __name__ == '__main__':
    unittest.main()