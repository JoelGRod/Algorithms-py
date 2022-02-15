"""
Consider a "word" as any sequence of capital letters A-Z (not limited 
to just "dictionary words"). For any word with at least two different 
letters, there are other words composed of the same letters but in a 
different order (for instance, STATIONARILY/ANTIROYALIST, which happen 
to both be dictionary words; for our purposes "AAIILNORSTTY" is also a 
"word" composed of the same letters as these two).

We can then assign a number to every word, based on where it falls in 
an alphabetically sorted list of all words made up of the same group 
of letters. One way to do this would be to generate the entire list 
of words and find the desired one, but this would be slow if the word 
is long.

Given a word, return its number. Your function should be able to accept 
any word 25 letters or less in length (possibly with some letters 
repeated), and take no more than 500 milliseconds to run. 
"""

from algorithms.main.maths.factorial import factorial

def list_position(word):
    """Return the anagram list position of the word"""
    if len(word) == 1: return 1         # Base Case

    sum_pos = list_position(word[1:])   # Recursive Case

    y = len(word)

    # Count chars in word and create a list of tuples
    counter = {}
    for char in word:
        if char in counter: counter[char] += 1
        else: counter[char] = 1
    
    # Multiply factorials of accumulated values
    fact_add = 1
    for accum in counter.values():
        fact_add *= factorial(accum)
    
    py = factorial(y) // fact_add
    
    # We need all the elements before first char 
    sorted_elem = sorted(counter.items())

    # Sum accumulated values of chars before first char
    sum_elem_before = 0
    for el in sorted_elem:
        if el[0] == word[0]: break
        sum_elem_before += el[1]
    
    return (
        (py // y * sum_elem_before) + sum_pos 
        if sum_elem_before != 0 
        else 0 + sum_pos)

################################################################
# Extra Solution I
# from math import factorial
# def listPosition(word):
#     """Return the anagram list position of the word"""
#     count = 0
#     while len(word) > 1:
#         first = word[0]
#         uniques = set(word)
#         possibilities = factorial(len(word))
#         for letter in uniques:
#             possibilities /= factorial(word.count(letter))
#         for letter in uniques:
#             if letter < first:
#                 count += possibilities / len(word) * word.count(letter)
#         word = word[1:]
#     return count +1

################################################################
# Extra Solution II
# from collections import Counter

# def listPosition(word):
#     l, r, s = len(word), 1, 1
#     c = Counter()

#     for i in range(l):
#         x = word[(l - 1) - i]
#         c[x] += 1
#         for y in c:
#             if (y < x):
#                 r += s * c[y] // c[x]
#         s = s * (i + 1) // c[x]
#     return r

################################################################
# Extra Solution III
# import math
# from collections import Counter

# def listPosition(word):
#     if len(word) == 1:
#         return 1
#     else:
#         return sorted(word).index(word[0]) * calc_word_perm(word) // len(word) + listPosition(word[1:])
        
# def calc_word_perm(word):
#     denom = 1
#     for count in Counter(word).values():
#         denom *= math.factorial(count)
#     return math.factorial(len(word))//denom