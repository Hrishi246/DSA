class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_start(self, data):
        self.size = self.size + 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_end(self, data):
        self.size = self.size + 1
        new_node = Node(data)
        actual_node = self.head

        # we have to find the end of the linked list in O(N) linear running time
        while actual_node.next_node is not None:
            actual_node = actual_node.next_node

        # actual_node is the last node: so we insert the new_node right after the actual_node
        actual_node.next_node = new_node

    def size_of_list(self):
        return self.size

    def traverse(self):
        actual_node = self.head

        if self.head is None:
            return

        else:
            while actual_node:
                print(actual_node.data)
                actual_node = actual_node.next_node

    def remove(self, data):
        actual_node = self.head
        previous_node = None

        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node =actual_node.next_node

        if actual_node is None:
            return

        if previous_node is None:
            self.head = actual_node.next_node
        else:
            previous_node.next_node = actual_node.next_node

    def get_middle_node(self):

        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer.next_node and fast_pointer.next_node.next_node:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node


        return slow_pointer

    # Interview Question #8
    # Construct an in-place algorithm to reverse a linked list!
    def reverse_list(self):
        actual_node = self.head
        previous = None
        next = None
        while actual_node:
            next = actual_node.next_node
            actual_node.next_node = previous
            previous = actual_node
            actual_node = next

        self.head = previous

if __name__ == '__main__':

    linked_list = LinkedList()
    linked_list.insert_start(1)
    linked_list.insert_end(2)
    linked_list.insert_end(3)

    # print(linked_list.get_middle_node().data)
    # linked_list.remove(2)
    linked_list.reverse_list()

    linked_list.traverse()
