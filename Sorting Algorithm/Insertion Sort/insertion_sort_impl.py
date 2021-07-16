def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j = j-1

if __name__ == '__main__':
    nums = [12,67,45,11,-90,100]
    insertion_sort(nums)
    print(nums)