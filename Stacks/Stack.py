
class Stack:

    def __init__(self):
        self.stack = []

    # O(1)
    def size_stack(self):
        return len(self.stack)

    # O(1) running time
    def is_empty(self):
        return self.stack == []

    # O(1) running time
    def push(self, data):
        self.stack.append(data)

    # O(1) because we manipulate the last item
    def pop(self):

        if self.size_stack() < 1:
            return None

        data = self.stack[-1]
        del self.stack[-1]
        return data

    # O(1) constant running time
    def peek(self):
        return self.stack[-1]

if __name__ == '__main__':
    main_stack = Stack()
    main_stack.push(1)
    main_stack.push(12)
    main_stack.push(6)
    main_stack.push(4)
