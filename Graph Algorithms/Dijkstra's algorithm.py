import heapq

class Edge:
    def __init__(self, start_node, target_node, weight):
        self.start_node = start_node
        self.target_node = target_node
        self.weight = weight

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.adjecency_list = []
        self.min_distance = float('inf')
        self.previous = None

    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance

class Dij_algorithm:
    def __init__(self):
        self.heap = []

    def calculate_distance_values(self, start_node):
        start_node.min_distance = 0
        heapq.heappush(self.heap, start_node)

        while self.heap:
            actual_node = heapq.heappop(self.heap)

            if actual_node.visited:
                continue

            for edge in actual_node.adjecency_list:
                u = edge.start_node
                v = edge.target_node
                new_distance = u.min_distance + edge.weight

                if new_distance < v.min_distance:
                    v.min_distance = new_distance
                    heapq.heappush(self.heap, v)
                    v.previous = u

            actual_node.visited = True
