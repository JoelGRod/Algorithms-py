from ...main.graph.dijkstra import dijkstra

# Example One
graph = {
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

costs = {
    "a": 5,
    "b": 2,
    "c": float("inf"),
    "d": float("inf"),
    "end": float("inf")
}

parents = {
    "a": "init",
    "b": "init",
    "c": None,
    "d": None,
    "end": None
}

print(dijkstra(graph, costs, parents))

# Example Two
graph_two = {
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

costs_two = {
    "a": 10,
    "b": float("inf"),
    "c": float("inf"),
    "end": float("inf")
}

parents_two = {
    "a": "init",
    "b": None,
    "c": None,
    "end": None
}

print(dijkstra(graph_two, costs_two, parents_two))