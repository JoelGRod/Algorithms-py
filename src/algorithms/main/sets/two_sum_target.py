"""
Given a target and a set of numbers, find the two numbers index in 
set where the sum gives the target using only a for loop
"""

input = [9, 4, 20, 3, 39, 12, 1, 4, 6]

def two_sum(input, target):
    differences = {}
    for idx, number in enumerate(input):
        difference = target - number
        if difference in differences:
            return [differences[difference]['i'], idx]
        differences[number] = {
            'value': target - number,
            'i': idx
        }
    return []

