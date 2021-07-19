# Interview Question #2
# "A palindrome is a string that reads the same forward and backward"
# For example: radar or madam
# Our task is to design an optimal algorithm for checking whether
# a given string is palindrome or not!

#my solution
def if_pallindrome(input_string):

    start_index = 0
    end_index = len(input_string) - 1

    while end_index > start_index:
        if input_string[start_index] != input_string[end_index]:
            return False
        start_index = start_index + 1
        end_index = end_index - 1

    return True

#course solution
def if_pallindrome_sol(input_string):
    return True if input_string == input_string[::-1] else False

print(if_pallindrome_sol("madam"))