# The problem is that we want to reverse a T[] array in O(N) linear time complexity
# and we want the algorithm to be in-place as well - so no additional memory can be used!
# For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]

#my solution
def reverse_array(input_array):

    if len(input_array)%2 == 0:
        for i in range(0, len(input_array)//2):
            input_array[i], input_array[len(input_array)-i-1] = input_array[len(input_array)-i-1], input_array[i]
    else:
        for i in range(0, (len(input_array)//2)+1):
            input_array[i], input_array[len(input_array)-i-1] = input_array[len(input_array)-i-1], input_array[i]

    return input_array

#course solution
def reverse_array_sol(input_array):

    start_index = 0
    end_index = len(input_array)-1

    while end_index > start_index:
        input_array[start_index], input_array[end_index] = input_array[end_index], input_array[start_index]
        start_index = start_index + 1
        end_index = end_index - 1

    return input_array



print(reverse_array_sol([1,2,3,4,7, 112]))