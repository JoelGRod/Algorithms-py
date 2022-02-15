import unittest
from algorithms.main.strings.list_position import list_position

class TestListPosition(unittest.TestCase):
    def test_list_position(self):
        test_values = {
            'A' : 1, 
            'ABAB' : 2, 
            'AAAB' : 1, 
            'BAAA' : 4, 
            'QUESTION' : 24572, 
            'BOOKKEEPER' : 10743
        }
        for word in test_values:
            self.assertEqual(list_position(word), test_values[word])


if __name__ == '__main__':
    unittest.main()