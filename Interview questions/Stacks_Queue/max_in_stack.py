class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    # O(1)
    def size_stack(self):
        return len(self.stack)

    # O(1) running time
    def is_empty(self):
        return self.stack == []

    # O(1) running time
    def push(self, data):
        self.stack.append(data)

        if len(self.stack) == 1:
            self.max_stack.append(data)
            return

        if data > self.max_stack[-1]:
            self.max_stack.append(data)
        else:
            self.max_stack.append(self.max_stack[-1])

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

    def max_in_stack(self):
        return self.max_stack[-1]


if __name__ == '__main__':
    main_stack = Stack()
    main_stack.push(1)
    main_stack.push(12)
    main_stack.push(6)
    main_stack.push(4)

    max_item = main_stack.max_in_stack()
    print(max_item)



