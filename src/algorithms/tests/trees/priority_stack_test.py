import unittest
from algorithms.main.trees.priority_stack import PriorityStack


class TestPriorityStack(unittest.TestCase):
    def test_priority_stack(self):
        pstack = PriorityStack()
        
        pstack.push("A", 2)
        pstack.push("B", 3)
        pstack.push("C", 2)
        pstack.push("D", 4)
        pstack.push("C", 3)

        result = []
        while not pstack.empty():
            result.append(str(pstack.pop()))

        self.assertEqual(result, '[“A",2],["C",3],["B",3],["D",4]')


if __name__ == '__main__':
    unittest.main()
