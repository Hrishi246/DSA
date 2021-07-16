
class Node():
    def __init__(self, name):
        self.name = name
        self.adjecency_list = []
        self.visited = False

def breadth_first_search(start_node):
    queue = [start_node]
    while queue:
        actual_node = queue.pop(0)
        actual_node.visited = True
        print(actual_node.name)
        for item in actual_node.adjecency_list:
            if not item.visited:
                queue.append(item)

if __name__ == "__main__":
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node8 = Node("H")

    node1.adjecency_list.append(node2)
    node1.adjecency_list.append(node6)
    node1.adjecency_list.append(node7)
    node2.adjecency_list.append(node3)
    node2.adjecency_list.append(node4)
    node4.adjecency_list.append(node5)
    node7.adjecency_list.append(node8)

    breadth_first_search(node1)


