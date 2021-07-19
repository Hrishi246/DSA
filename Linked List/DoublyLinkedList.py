class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #We are inserting a new node at the end of the linked list
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node


    def traverse_forward(self):
        actual_node = self.head
        print("traversing forward...")
        while actual_node:
            print(actual_node.data)
            actual_node = actual_node.next_node

    def traverse_backward(self):
        actual_node = self.tail
        print("traversing backward...")
        while actual_node:
            print(actual_node.data)
            actual_node = actual_node.previous_node



if __name__ == '__main__':
    d_list = DoublyLinkedList()
    d_list.insert(1)
    d_list.insert(2)
    d_list.insert(3)

    d_list.traverse_forward()
    d_list.traverse_backward()