"""
Find all prime factors of a given number
"""


def prime_factors(n):
    primes = []
    c = 2
    while n > 1:
        if n % c == 0:
            primes.append(int(c))
            n /= c
        else:
            c += 1
    return primes
