# Interview Question #3
# Our task is to design an efficient algorithm to reverse a given integer.
# For example if the input of the algorithm is 1234 then the output should be 4321.

def reverse_integer(input_integer):

    quotient, remainder = divmod(input_integer, 10)
    result = 0
    while quotient > 0:
        result = (result + remainder)*10
        quotient, remainder = divmod(quotient, 10)

    return result + remainder

print(reverse_integer(4754906))



