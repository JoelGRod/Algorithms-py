import unittest
from algorithms.main.trees.priority_stack import PriorityStack


class TestPriorityStack(unittest.TestCase):

    pstack = PriorityStack()

    def test_priority_stack(self):
        # Arrange
        self.pstack.push("A", 2)
        self.pstack.push("B", 3)
        self.pstack.push("C", 2)
        self.pstack.push("D", 4)
        self.pstack.push("C", 3)

        # Act
        result = []
        while not self.pstack.empty():
            result.append(str(self.pstack.pop()))

        # Assert
        result = ",".join(result)
        expected = "['A', 2],['C', 3],['B', 3],['D', 4]"
        self.assertEqual(result, expected)

    def test_priority_stack_extra(self):
        # Arrange
        self.pstack.push("A", 2)
        self.pstack.push("B", 3)
        self.pstack.push("C", 2)
        self.pstack.push("D", 4)
        self.pstack.push("C", 3)
        self.pstack.push("56 2", 56)
        self.pstack.push("34", 34)
        self.pstack.push("56 1", 56)
        self.pstack.push("1 3", 1)
        self.pstack.push("1 2", 1)
        self.pstack.push("1 1", 1)
        self.pstack.push("187 2", 187)
        self.pstack.push("187 1", 187)

        # Act
        result = []
        while not self.pstack.empty():
            result.append(str(self.pstack.pop()))

        # Assert
        result = ",".join(result)
        expected = ("['1 1', 1],['1 2', 1],['1 3', 1],['A', 2]," +
                    "['C', 3],['B', 3],['D', 4],['34', 34],['56 1', 56]," + 
                    "['56 2', 56],['187 1', 187],['187 2', 187]")
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
