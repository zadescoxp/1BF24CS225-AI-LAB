import heapq

def astar(graph, start, goal, h):
    pq = [(h[start], 0, start)]
    cost = {start: 0}

    while pq:
        f, g, node = heapq.heappop(pq)

        if node == goal:
            return g

        if g != cost[node]:
            continue

        for child, w in graph.get(node, []):
            new_g = g + w

            if child not in cost or new_g < cost[child]:
                cost[child] = new_g
                heapq.heappush(pq, (new_g + h[child], new_g, child))

    return -1

graph = {'A': [('B', 1), ('C', 4)], 'B': [('D', 2)], 'C': [('D', 1)], 'D': []}
h = {'A': 3, 'B': 2, 'C': 1, 'D': 0}
print(astar(graph, 'A', 'D', h))
