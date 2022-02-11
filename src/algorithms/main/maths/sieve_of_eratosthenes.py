"""
    The Sieve of Eratosthenes is an algorithm for finding all 
    prime numbers up to some limit n.

    It is attributed to Eratosthenes of Cyrene, an ancient Greek mathematician.
"""


def sieve_of_eratosthenes(limit):
    is_prime = [True for n in range(limit + 1)]
    is_prime[0] = False
    is_prime[1] = False

    primes = []

    for number in range(2, limit + 1):
        if is_prime[number] == True:
            primes.append(number)

            next_number = number * number

            while next_number <= limit:
                is_prime[next_number] = False
                next_number += number
    
    return primes
