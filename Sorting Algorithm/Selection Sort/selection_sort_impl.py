def selection_sort(nums):

    for i in range(len(nums)-1):
        index = i
        for j in range(i,len(nums)):
            if nums[j] < nums [index]:
                index = j

        if index != i:
            nums[i], nums[index] = nums[index], nums[i]

if __name__ == '__main__':
    nums = [12,67,45,11,-90,100]
    selection_sort(nums)
    print(nums)