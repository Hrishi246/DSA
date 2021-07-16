import random

class BogoSort:
    def __init__(self, nums):
        self.nums = nums


    def is_sorted(self):
        for i in range(len(self.nums)-1):
            if self.nums[i] > self.nums[i+1]:
                return False

        return True

    def shuffle(self):
        for i in range(len(self.nums)-2,0,-1):
            j = random.randint(0,i+1)
            self.nums[i], self.nums[j] = self.nums[i], self.nums[j]

    def sort(self):
        while not self.is_sorted():
            print("Shuffle again...")
            self.shuffle()

if __name__ == '__main__':
    algo = BogoSort([-6,-3, -8])
    algo.sort()

    print(algo.nums)


