""" Sum List Digits
"""

def sum_digits(numbers):
    if len(numbers) == 1: return numbers[0]
    return numbers[0] + sum_digits(numbers[1:])

print(sum_digits([1,2,3,4,5,6,7]))