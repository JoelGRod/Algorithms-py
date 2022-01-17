from collections import deque

""" Breadth First Search - BFS
    a - Is there a path between node A and node B?
    b - Which is the shorter path between node A and node B?
    For:
        Directed graph
        Unweighted graph
"""

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

def breadth_first_search(name):
    queue = deque()
    queue += graph[name]
    visited = []

    while queue:
        person = queue.popleft()
        if not person in visited:
            if is_seller(person):
                return f"{person} is seller"
            else:
                visited.append(person)
                queue += graph[person]
    
    return f"There is no seller"


def is_seller(name):
    return name[-1] == "m"

print(breadth_first_search("Joe"))