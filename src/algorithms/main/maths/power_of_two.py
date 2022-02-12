"""
    In mathematics, a power of two is a number of the form 2n where n is an 
    integer, that is, the result of exponentiation with number two as the 
    base and integer n as the exponent. 
    In a context where only integers are considered, n is restricted to non-negative 
    values, so we have 1, 2, and 2 multiplied by itself a certain number of 
    times.
    Because two is the base of the binary numeral system, powers of two are common 
    in computer science. Written in binary, a power of two always has the form 
    100…000 or 0.00…001, just like a power of ten in the decimal system.
"""

def power_of_two_naive(test_number):
    while test_number > 1:
        if test_number % 2 != 0: return False
        test_number /= 2
    return True if test_number == 1 else False


def power_of_two(test_number):
    if test_number < 1: return False
    return (test_number & (test_number - 1)) == 0

