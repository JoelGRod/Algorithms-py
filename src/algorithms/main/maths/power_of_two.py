

def power_of_two_naive(test_number):
    while test_number > 1:
        if test_number % 2 != 0: return False
        test_number /= 2
    return True if test_number == 1 else False


def power_of_two(test_number):
    if test_number < 1: return False
    return (test_number & (test_number - 1)) == 0

