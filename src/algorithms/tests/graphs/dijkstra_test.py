import unittest
from algorithms.main.graphs.dijkstra import dijkstra

# Example One
graph = {
    "init": {
        "a": 6,
        "b": 2
    },
    "a": {
        "end": 1
    },
    "b": {
        "a": 3,
        "end": 5
    },
    "end": {}
}

costs = {
    "a": 6,
    "b": 2,
    "end": float("inf")
}

parents = {
    "a": "init",
    "b": "init",
    # "end": None
}

# Example Two
graph_two = {
    "init": {
        "a": 5,
        "b": 2,
    },
    "a": {
        "c": 4,
        "d": 2
    },
    "b": {
        "a": 8,
        "d": 7
    },
    "c": {
        "end": 3,
        "d": 6
    },
    "d": {
        "end": 1
    },
    "end": {}
}

costs_two = {
    "a": 5,
    "b": 2,
    "c": float("inf"),
    "d": float("inf"),
    "end": float("inf")
}

parents_two = {
    "a": "init",
    "b": "init",
    "c": None,
    "d": None,
    "end": None
}

# Example Three
graph_three = {
    "init": {
        "a": 10
    },
    "a": {
        "b": 20
    },
    "b": {
        "c": 1,
        "end": 30
    },
    "c": {
        "a": 1
    },
    "end": {}
}

costs_three = {
    "a": 10,
    "b": float("inf"),
    "c": float("inf"),
    "end": float("inf")
}

parents_three = {
    "a": "init",
    "b": None,
    "c": None,
    "end": None
}

class TestDijkstra(unittest.TestCase):
	def test_dijkstra_example_one(self):
		expected = (
            {'a': 'b', 'b': 'init', 'end': 'a'}, 
            {'a': 5, 'b': 2, 'end': 6}
        )
		self.assertEqual(dijkstra(graph, costs, parents), expected)

	def test_dijkstra_example_two(self):
		expected = (
            {'a': 'init', 'b': 'init', 'c': 'a', 'd': 'a', 'end': 'd'}, 
            {'a': 5, 'b': 2, 'c': 9, 'd': 7, 'end': 8}
        )
		self.assertEqual(dijkstra(graph_two, costs_two, parents_two), expected)

	def test_dijkstra_example_three(self):
		expected = (
            {'a': 'init', 'b': 'a', 'c': 'b', 'end': 'b'}, 
            {'a': 10, 'b': 30, 'c': 31, 'end': 60}
        )
		self.assertEqual(dijkstra(graph_three, costs_three, parents_three), expected)


if __name__ == '__main__':
    unittest.main()