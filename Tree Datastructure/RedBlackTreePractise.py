class color:
    RED = 1
    BLACK = 2

class Node:
    def __init__(self, data, parent=None, color = color.RED):
        self.data = data
        self.parent = parent
        self.color = color
        self.left_node = None
        self.right_node = None

class RedBlackTree:
    def __init__(self):
        self.root = None

    def is_red(self, node):
        if node is None:
            return False
        else:
            return node.color == color.RED

    def violate(self, node):
        while self.is_red(node) and self.is_red(node.parent) and node != self.root:
            parent_node = node.parent
            grandparent_node = parent_node.parent

            if parent_node == grandparent_node.left_node:
                uncle = grandparent_node.right_node
                # case 1 and  case 4
                if uncle and self.is_red(uncle):
                    print("Recoloring grandparent node to red ", grandparent_node.data)
                    grandparent_node.color = color.RED
                    print("Recoloring parent node to black ", parent_node.data)
                    parent_node.color = color.BLACK
                    uncle.color = color.BLACK
                    node = grandparent_node
                else:
                    #if uncle node is black





    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            self.violate(self.root)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):

        if data < node.data:
            if node.left_node:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data,node)
                self.violate(node.left_node)

        else:
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data,node)
                self.violate(node.right_node)

    def traverse(self):
        if self.root:
            self.in_order_traversal(self.root)

    def in_order_traversal(self, node):

        if node.left_node:
            self.in_order_traversal(node.left_node)

        print(node.data)

        if node.right_node:
            self.in_order_traversal(node.right_node)

    def right_rotation(self, node):
        print("Rotating to the right on node ", node.data)

        temp_left_node = node.left_node
        t = temp_left_node.right_node

        temp_left_node.right_node = node
        node.left_node = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        temp_left_node.parent = temp_parent
        node.parent = temp_left_node

        if temp_left_node.parent is not None and temp_left_node.parent.left_node == node:
            temp_parent.left_node = temp_left_node

        if temp_left_node.parent is not None and temp_left_node.parent.right_node == node:
            temp_parent.right_node = temp_left_node

        if node == self.root:
            self.root = temp_left_node

    def left_rotation(self, node):
        print("Rotating to the left on node ", node.data)

        temp_right_node = node.right_node
        t = temp_right_node.left_node

        temp_right_node.left_node = node
        node.right_node = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        temp_right_node.parent = temp_parent
        node.parent = temp_right_node

        if temp_right_node.parent is not None and temp_right_node.parent.left_node == node:
            temp_parent.left_node = temp_right_node

        if temp_right_node.parent is not None and temp_right_node.parent.right_node == node:
            temp_parent.right_node = temp_right_node

        if node == self.root:
            self.root = temp_right_node
