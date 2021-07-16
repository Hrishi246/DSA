NO_OF_BUCKETS = 10

class RadixSort:

    def __init__(self, data):
        self.data = data
        self.counting_array = [[] for _ in range(NO_OF_BUCKETS)]

    def get_digits(self):
        return len(str(max(self.data)))

    def radix_sort(self, digit):
        for num in self.data:
            index = (num // (10 ** digit)) % 10
            self.counting_array[index].append(num)

        #WE HAVE TO CONSIDER ALL THE ITEMS IN COUNT ARRAY
        z =0
        for i in range(len(self.counting_array)):
            while len(self.counting_array[i]) > 0:
                self.data[z] = self.counting_array[i].pop(0)
                z = z + 1

    def counting_sort(self):
        for d in range(self.get_digits()):
            self.radix_sort(d)

if __name__ == '__main__':
    numbers = [12,234,11,101,106,100]
    radix = RadixSort(numbers)
    radix.counting_sort()
    print(radix.data)