# Interview Question #5
# The problem is that we want to find duplicates in a one-dimensional array
# of integers in O(N) running time where the integer values are smaller than
# the length of the array!
# For example: if we have a list [1, 2, 3, 1, 5] then the algorithm can detect
# that there are a duplicate with value 1.
# Note: the array can not contain items smaller than 0 and items with
# values greater than the size of the list.
# This is how we can achieve O(N) linear running time complexity!

def find_duplicates(input_array):
    duplicates = []
    for i in range(len(input_array)):
        if input_array[abs(input_array[i])] > 0:
            input_array[abs(input_array[i])] = -1*input_array[abs(input_array[i])]
        else:
            duplicates.append(abs(input_array[abs(input_array[i])]))

    return duplicates

print(find_duplicates([2,3,1,2,4,3]))

