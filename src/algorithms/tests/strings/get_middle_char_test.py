import unittest
from algorithms.main.strings.get_middle_char import get_middle

class TestMiddleChar(unittest.TestCase):
    def test_get_middle_char(self):
        self.assertEqual(get_middle("test"),"es")
        self.assertEqual(get_middle("testing"),"t")
        self.assertEqual(get_middle("middle"),"dd")
        self.assertEqual(get_middle("A"),"A")
        self.assertEqual(get_middle("of"),"of")


if __name__ == '__main__':
    unittest.main()