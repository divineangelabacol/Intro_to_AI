import heapq

graph = {
    "Sinamar 1": [("Sunrise St", 1.5), ("USM Ave", 2)],
    "Sunrise St": [("Sinamar 1", 1.5), ("Bai Marabay Plang Ave", 2)],
    "USM Ave": [("Sinamar 1", 2), ("Villanueva 1", 3)],
    "Bai Marabay Plang Ave": [("Sunrise St", 2), ("Villanueva 1", 2.5)],
    "Villanueva 1": []
}

heuristic = {
    "Sinamar 1": 5,
    "Sunrise St": 3,
    "USM Ave": 2,
    "Bai Marabay Plang Ave": 2,
    "Villanueva 1": 0
}

def astar(start, goal):
    queue = []
    heapq.heappush(queue, (0, start, []))
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node in visited:
            continue

        path = path + [node]
        visited.add(node)

        if node == goal:
            return path

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                g = cost + weight
                h = heuristic[neighbor]
                f = g + h
                heapq.heappush(queue, (f, neighbor, path))

    return None


route = astar("Sinamar 1", "Villanueva 1")

print("Fastest Route:")
print(" -> ".join(route))