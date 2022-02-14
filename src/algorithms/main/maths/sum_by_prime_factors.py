""" INCOMPLETE
Given an array of positive or negative integers

I= [i1,..,in]

you have to produce a sorted array P of the form

[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers. 
The final result has to be given as a string in Java, C#, C, C++ 
and as an array of arrays in other languages.

Example:
I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

Notes:

It can happen that a sum is 0 if some numbers are negative!
Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, 
the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result 
amongst others.
"""


def sum_for_list(lst):
    primes = set()
    for num in lst:
        primes.update([p for p in sieve_of_eratosthenes(abs(num)) if num % p == 0])

    result = []

    for p in primes:
        sum = 0
        for num in lst:
            if abs(num) % p == 0:
                sum += num
        result.append([p, sum])

    return result


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

# Faster than Sieve of...
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
