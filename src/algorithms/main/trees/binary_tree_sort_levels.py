"""
You are given a binary tree:

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

Your task is to return the list with elements from tree sorted by levels, 
which means the root element goes first, then root children 
(from left to right) are second and third, and so on.

Return empty list if root is None.

Example 1 - following tree:
                 2
            8        9
          1  3     4   5

Should return following list:
[2,8,9,1,3,4,5]

Example 2 - following tree:
                 1
            8        4
              3        5
                         7

Should return following list:
[1,8,4,3,5,7]

"""


from collections import deque   # Example 4


def tree_by_levels(node):
    values = []
    nodes_queue = []

    if node != None:
        nodes_queue.append(node)

    while(nodes_queue):
        temp_node = nodes_queue.pop(0)
        values.append(temp_node.value)
        if temp_node.left != None:
            nodes_queue.append(temp_node.left)
        if temp_node.right != None:
            nodes_queue.append(temp_node.right)

    return values


def tree_by_levels_two(tree):
    queue = [tree]
    values = []

    while queue:
        node = queue.pop(0)
        if node:
            queue += [node.left, node.right]
            values.append(node.value)

    return values


def tree_by_levels_three(a):
    q, w = [a], []
    while q := [y for x in q if x for y in w.append(x.value) or [x.left, x.right]]:
        continue
    return w


def tree_by_levels_four(node):
    if not node:
        return []
    res, queue = [], deque([node, ])
    while queue:
        n = queue.popleft()
        res.append(n.value)
        if n.left is not None:
            queue.append(n.left)
        if n.right is not None:
            queue.append(n.right)
    return res
