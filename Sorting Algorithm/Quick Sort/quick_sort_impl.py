
class QuickSort:
    def __init__(self, data):
        self.data = data

    def partition(self, low, high):

        pivot_index = (low + high) // 2

        self.data[pivot_index], self.data[high] = self.data[high], self.data[pivot_index]

        for i in range(low, high):
            if self.data[i] < self.data[high]:
                self.data[i], self.data[low] = self.data[low], self.data[i]
                low = low + 1

        self.data[low], self.data[high] = self.data[high], self.data[low]

        return low

    def quick_sort(self, low, high):
        if low >= high:
            return
        pivot_index = self.partition(low, high)

        self.quick_sort(low, pivot_index -1)
        self.quick_sort(pivot_index + 1, high)


    def sort(self):
        self.quick_sort(0, len(self.data)-1)
        
if __name__ == '__main__':
    data = [10, -4, 0, 3, 2, 1, 100, -8]
    quick_algo = QuickSort(data)
    quick_algo.sort()
    print(data)