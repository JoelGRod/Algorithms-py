""" Dijkstra - O(( V + E ) log V)
    a - Is there a path between node A and node B?
    b - Which is the faster (not shorter) path between node A and node B?
    For:
        Directed graph
        Weighted graphs
        Non-cyclic graphs
        Non negative edges
    Greedy - approximation / Brute force Algorithm
"""

# All nodes are required
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

# All nodes are required, non init nodes are infinite
costs = {
    "a": 6,
    "b": 2,
    "end": float("inf")
}

# Only init nodes are required
parents = {
    "a": "init",
    "b": "init",
    # "end": None
}

def find_least_cost_node(costs, processed):
    lower_cost = float("inf")
    least_cost_node = None
    for node in costs:
        cost = costs[node]
        if lower_cost > cost and node not in processed:
            lower_cost = cost
            least_cost_node = node
    return least_cost_node

def dijkstra(graph, costs, parents):
    processed = []
    node = find_least_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors:
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_least_cost_node(costs, processed)
    return parents, costs

# print(dijkstra(graph, costs, parents))

