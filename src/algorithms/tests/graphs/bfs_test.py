import unittest
from algorithms.main.graphs.bfs import breadth_first_search as bfs

graph = {
    "Joe": ["Claire", "Bob", "Alice"],
    "Claire": ["Thom", "Jhonny"],
    "Bob": ["Anuj", "Peggy"],
    "Alice": ["Peggy"],
    "Thom": [],
    "Jhonny": [],
    "Anuj": [],
    "Peggy": []
}

graph_fails = {
    "Joe": ["Claire", "Bob", "Alice"],
    "Claire": ["Maikel", "Jhonny"],
    "Bob": ["Anuj", "Peggy"],
    "Alice": ["Peggy"],
    "Maikel": [],
    "Jhonny": [],
    "Anuj": [],
    "Peggy": []
}

class TestBreadFirstSearch(unittest.TestCase):
	def test_bfs_is_seller(self):
		expected = 'Thom is seller'
		self.assertEqual(bfs(graph, "Joe"), expected)

	def test_bfs_there_is_no_seller(self):
		expected = 'There is no seller'
		self.assertEqual(bfs(graph_fails, "Joe"), expected)

# if __name__ == '__main__':
#     unittest.main()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestBreadFirstSearch('test_bfs_is_seller'))
    suite.addTest(TestBreadFirstSearch('test_bfs_there_is_no_seller'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())