class Node():

    def __init__(self, name):
        self.name = name
        self.adjecency_list = []
        self.visited = False

def depth_first_search(start_node):
    stack = [start_node]
    while stack:
        #the pop function returns with the last item we inserted 0(1)
        actual_node = stack.pop()
        actual_node.visited = True
        print(actual_node.name)
        for item in actual_node.adjecency_list:
            if not item.visited:
                stack.append(item)

if __name__ == "__main__":
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    node1.adjecency_list.append(node2)
    node1.adjecency_list.append(node3)
    node2.adjecency_list.append(node4)
    node4.adjecency_list.append(node5)

    depth_first_search(node1)


