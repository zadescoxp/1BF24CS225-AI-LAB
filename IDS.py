def dls(graph, node, goal, depth):
    if node == goal:
        return True
    if depth == 0:
        return False

    for child in graph.get(node, []):
        if dls(graph, child, goal, depth - 1):
            return True

    return False

def ids(graph, start, goal):
    for depth in range(100):
        if dls(graph, start, goal, depth):
            return True
    return False

graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], 'D': [], 'E': []}
print(ids(graph, 'A', 'E'))
