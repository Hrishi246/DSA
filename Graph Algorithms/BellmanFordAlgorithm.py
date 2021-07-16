class Edge:
    def __init__(self, weight, start_node, target_node):
        self.start_node = start_node
        self.target_node = target_node
        self.weight = weight

class Node:
    def __init__(self, name):
        self.name = name
        self.min_distance = float('inf')
        self.previous = None
        self.adjacency_list = []

class BellmanFordAlgorithm:
    def __init__(self, node_list, edge_list, starting_node):
        self.node_list = node_list
        self.edge_list = edge_list
        self.starting_node = starting_node
        self.has_negative_cycle = False

    def calculate_distances(self):
        self.starting_node.min_distance = 0
        for _ in range(len(self.node_list) - 1):
            for edge in self.edge_list:
                u = edge.start_node
                v = edge.target_node
                distance = u.min_distance + edge.weight
                if distance < v.min_distance:
                    v.min_distance = distance
                    v.previous = u

        for last_iter_edge in self.edge_list:
            u = last_iter_edge.start_node
            v = last_iter_edge.target_node
            distance = u.min_distance + last_iter_edge.weight
            if distance < v.min_distance:
                print("Negative Cycle detected")
                self.has_negative_cycle = True
                break

    def get_shortest_path(self, node):
        if not self.has_negative_cycle:
            print("The shortest path to given node from starting vertex is ", node.min_distance)
            actual = node
            while actual is not None:
                print(actual.name)
                actual = actual.previous
        else:
            print("There is negative cycle in graph G(V,E)")

if __name__ == '__main__':
    # we have to create the vertices
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")

    # let's create the edges
    edge1 = Edge(5, node1, node2)
    edge2 = Edge(9, node1, node5)
    edge3 = Edge(4, node2, node5)
    edge4 = Edge(12, node2, node3)
    edge5 = Edge(7, node2, node4)
    edge6 = Edge(3, node3, node4)
    edge7 = Edge(1, node3, node6)
    edge8 = Edge(9, node4, node7)
    edge9 = Edge(6, node5, node3)
    edge10 = Edge(4, node5, node6)
    edge11 = Edge(2, node6, node7)
    edge12 = Edge(6, node7, node3)

    # handle the adjacency lists
    node1.adjacency_list.append(edge1)
    node1.adjacency_list.append(edge2)
    node2.adjacency_list.append(edge3)
    node2.adjacency_list.append(edge4)
    node2.adjacency_list.append(edge5)
    node3.adjacency_list.append(edge6)
    node3.adjacency_list.append(edge7)
    node4.adjacency_list.append(edge8)
    node5.adjacency_list.append(edge9)
    node5.adjacency_list.append(edge10)
    node6.adjacency_list.append(edge11)
    node7.adjacency_list.append(edge12)

    # run the algorithm
    vertices = (node1, node2, node3, node4, node5, node6, node7)
    edges = (edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12)

    algorithm = BellmanFordAlgorithm(vertices, edges, node1)
    algorithm.calculate_distances()
    algorithm.get_shortest_path(node7)




