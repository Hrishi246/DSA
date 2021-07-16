class CountingSort:
    def __init__(self, data):
        self.data = data
        self.counting_array = [0 for i in range(max(self.data)-min(self.data) + 1)]

    def counting_sort(self):
        for i in range(len(self.data)):
            self.counting_array[self.data[i] - min(self.data)] += 1

        z = 0
        for i in range(min(self.data), max(self.data) + 1):
            while self.counting_array[i-min(self.data)] > 0:
                self.data[z] = i
                z = z + 1
                self.counting_array[i - min(self.data)] -= 1




if __name__ == '__main__':
    my_list = [1,4,1,7,1,10,-1,3]
    c_sort = CountingSort(my_list)
    print(c_sort.data)
    c_sort.counting_sort()
    print(c_sort.data)