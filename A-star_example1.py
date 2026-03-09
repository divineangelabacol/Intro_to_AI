import heapq

# Graph of USM Kabacan locations (node : [(neighbor, distance)])
graph = {
    "Main Gate": [("7-Eleven USM Kabacan", 1.5), ("Kabacan Wesleyan Academy", 1)],
    "7-Eleven USM Kabacan": [("Main Gate", 1.5), ("President Ave", 1.5)],
    "Kabacan Wesleyan Academy": [("Main Gate", 1), ("Coco Exit", 1.5)],
    "President Ave": [("7-Eleven USM Kabacan", 1.5), ("Mahogany Ave", 2)],
    "Mahogany Ave": [("President Ave", 2), ("Founder Ave Left Side", 1.5), ("Magasaysa Ave", 2)],
    "Founder Ave Left Side": [("Mahogany Ave", 1.5), ("Magasaysa Ave", 1.5), ("USM Science and Technology Building", 2)],
    "Magasaysa Ave": [("Mahogany Ave", 2), ("Founder Ave Left Side", 1.5), ("USM Science and Technology Building", 1.5)],
    "USM Science and Technology Building": [("Magasaysa Ave", 1.5), ("Founder Ave Left Side", 2), ("USM College of Medicine", 2), ("College of Engineering and Information Technology", 3)],
    "USM College of Medicine": [("USM Science and Technology Building", 2), ("Pomelo Ave", 1.5), ("College of Engineering and Information Technology", 2.5)],
    "Pomelo Ave": [("USM College of Medicine", 1.5), ("College of Engineering and Information Technology", 2)],
    "College of Engineering and Information Technology": [("Pomelo Ave", 2), ("USM College of Medicine", 2.5), ("USM Science and Technology Building", 3)],
    "Coco Exit": [("Kabacan Wesleyan Academy", 1.5)],
    "USCAO": []
}

# Heuristic estimate to goal (College of Engineering and Information Technology)
heuristic = {
    "Main Gate": 8,
    "7-Eleven USM Kabacan": 7.5,
    "Kabacan Wesleyan Academy": 9,
    "President Ave": 6.5,
    "Mahogany Ave": 5.5,
    "Founder Ave Left Side": 4.5,
    "Magasaysa Ave": 4,
    "USM Science and Technology Building": 3,
    "USM College of Medicine": 2.5,
    "Pomelo Ave": 2,
    "College of Engineering and Information Technology": 0,
    "Coco Exit": 10,
    "USCAO": 6
}

def astar(start, goal):
    queue = []
    heapq.heappush(queue, (0, start, []))

    visited = set()

    while queue:
        (cost, node, path) = heapq.heappop(queue)

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


start = "7-Eleven USM Kabacan"
goal = "College of Engineering and Information Technology"

route = astar(start, goal)

print("Shortest Route in USM:")
print(" -> ".join(route))