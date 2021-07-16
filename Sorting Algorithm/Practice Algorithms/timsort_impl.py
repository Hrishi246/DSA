def merge_sort(nums):

    if len(nums) <= 64:
        for i in range(len(nums)):
            j = i
            while j > 0 and nums[j] < nums[j-1]:
                nums[j], nums[j - 1] = nums[j-1], nums[j]
                j = j -1

        return

    middle_item = len(nums)//2

    left_sub = nums[:middle_item]
    right_sub = nums[middle_item:]

    merge_sort(left_sub)
    merge_sort(right_sub)

    i = 0
    j = 0
    k = 0

    while i < len(left_sub) and j < len(right_sub):
        if left_sub[i] < right_sub[j]:
            nums[k] = left_sub[i]
            i = i + 1

        else:
            nums[k] = right_sub[j]
            j = j + 1

        k = k + 1


    while i < len(left_sub):
        nums[k] = left_sub[i]
        i = i + 1
        k = k + 1

    while j < len(right_sub):
        nums[k] = right_sub[j]
        j = j + 1
        k = k + 1

if __name__ == '__main__':
    my_list = [12,5,18,-76,-74,234,167, 120, 0]
    merge_sort(my_list)
    print(my_list)