CAPACITY = 10

#the root node will be the largest node
class Heap:
    def __init__(self):
        #the actual number of items in data structure
        self.heap_size = 0
        #the underlying data structure
        self.heap = [0]* CAPACITY

    def insert(self, item):
        #When the heap is full we are not insert anymore items
        if self.heap_size == CAPACITY:
            return

        self.heap[self.heap_size] =  item
        self.heap_size = self.heap_size + 1

        #check the heap propeties
        self.fix_up(self.heap_size - 1)

    # starting with actual node we have intersted we have to follow-up
    #till root node to identify wheather we have to perform swap operation
    # O(Log N) time complexity
    def fix_up(self, index):

        parent_index = (index - 1)//2
        # We consider all the items until we hit the roor node, if the heap
        #property is violated we use the swap
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.fix_up(parent_index)

    #peek function returns maximum item in o(1) time complexity
    def get_max(self):
        return self.heap[0]

    #returns the max item and removes it as well
    #remove the root node of heap
    def poll(self):
        max_item = self.get_max()
        #swap the root node with last item and check heapify condition
        self.heap[0], self.heap[self.heap_size-1] = self.heap[self.heap_size-1], self.heap[0]
        self.heap_size = self.heap_size - 1

        # make sure heap is "heapify"
        self.fix_down(0)
        return max_item

    #starting with root node downwards until heap properties are not violated
    def fix_down(self, index):
        index_left = 2*index + 1
        index_right = 2*index + 2

        largest_index = index
        if index_left < self.heap_size and self.heap[index_left] > self.heap[index]:
            largest_index = index_left
        if index_right < self.heap_size and self.heap[index_right] > self.heap[largest_index]:
            largest_index = index_right
        if index != largest_index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self.fix_down(largest_index)

    def heap_sort(self):
        for _ in range(self.heap_size):
            max_item = self.poll()
            print(max_item)


if __name__ == "__main__":
    heap = Heap()
    heap.insert(13)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(8)
    heap.insert(1)
    heap.insert(-5)
    heap.insert(99)

    print(heap.heap)

    print(heap.heap_sort())







