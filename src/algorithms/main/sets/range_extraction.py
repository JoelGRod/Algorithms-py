"""
A format for expressing an ordered list of integers is to use a comma 
separated list of either

    individual integers

    or a range of integers denoted by the starting integer separated 
    from the end integer in the range by a dash, '-'. The range 
    includes all integers in the interval including both endpoints. 
    It is not considered a range unless it spans at least 3 numbers. 
    For example "12,13,15-17"

Complete the solution so that it takes a list of integers in 
increasing order and returns a correctly formatted string in the 
range format.

Example:

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
"""

from operator import itemgetter
from itertools import groupby


def solution(args):
    ranges = []

    for k, g in groupby(enumerate(args), lambda x: x[0]-x[1]):
        nums = [str(num) for num in list(map(itemgetter(1), g))]
        if len(nums) > 2:
            ranges.append(f"{nums[0]}-{nums[-1]}")
        if len(nums) == 2:
            ranges.append(f"{nums[0]},{nums[1]}")
        if len(nums) == 1:
            ranges.append(f"{nums[0]}")

    return ",".join(ranges)

def solution_extra(args):
    out = []
    beg = end = args[0]
    
    for n in args[1:] + [""]:        
        if n != end + 1:
            if end == beg:
                out.append( str(beg) )
            elif end == beg + 1:
                out.extend( [str(beg), str(end)] )
            else:
                out.append( str(beg) + "-" + str(end) )
            beg = n
        end = n
    
    return ",".join(out)