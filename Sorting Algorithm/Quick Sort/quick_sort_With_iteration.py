from collections import deque

class QuickSortIterative:
    def __init__(self, data):
        self.data = data

    def partition(self, low, high):
        pivot = low + high // 2
        self.data[pivot], self.data[high] = self.data[high], self.data[pivot]

        for i in range(low, high):
            if self.data[i] < self.data[high]:
                self.data[low], self.data[i] = self.data[i], self.data[low]
                low = low + 1

        self.data[low], self.data[high] = self.data[high] , self.data[low]

        return low


    def sort(self):
        stack = deque()
        stack.append((0, len(self.data)-1))

        while stack:
            start, end = stack.pop()
            #PARTITION PHASE
            pivot = self.partition(start, end)

            # CONQUER PHASE
            if pivot -1 > start:
                stack.append((start, pivot-1))

            if pivot + 1 < end:
                stack.append((pivot+1, end))


if __name__ == '__main__':
    n = [5, 4, 3, 2, 1]
    sort = QuickSortIterative(n)
    sort.sort()
    print(sort.data)