""" Factorial
"""

def factorial(value):
    if value == 1: return 1             # Base Case
    return value * factorial(value - 1) # Recursive Case

print(factorial(5))