# Interview Question #4
# Construct an algorithm to check whether two words (or phrases) are anagrams or not!
# "An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# "typically using all the original letters exactly once"
# For example: restful and fluster

def if_anagram(first_word, second_word):

    if len(first_word) != len(second_word):
        return False

    for i in first_word:
        if i not in second_word:
            return False

    return True


print(if_anagram("ullu","uull"))