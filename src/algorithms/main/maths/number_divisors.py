"""
Create a function named divisors/Divisors that takes an integer n > 1 and 
returns an array with all of the integer's divisors(except for 1 and the 
number itself), from smallest to largest. If the number is prime return 
the string '(integer) is prime'.

Example:
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
"""

def divisors(integer):
    divisors = [num for num in range(2, integer) if integer % num == 0]
    return f"{integer} is prime" if len(divisors) == 0 else divisors