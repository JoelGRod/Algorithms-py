"""
You will be given an array of numbers. You have to sort the odd numbers 
in ascending order while leaving the even numbers at their original 
positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
"""


def sort_array(source_array):
    # Return a sorted array.
    numbers = list(map(lambda number:
                       " " if number % 2 != 0
                       else number, source_array))
    odds = sorted([odd for odd in source_array if odd % 2 != 0])
    return list(map(lambda number:
                    odds.pop(0)
                    if number == " "
                    else number, numbers))


def sort_array_extra(arr):
    odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in arr]


def sort_array_extra_two(source_array):
    odds = sorted([odd for odd in source_array if odd % 2 != 0])
    return list(map(lambda number:
                    number if number % 2 == 0
                    else odds.pop(0), source_array))


def sort_array_extra_three(source_array):
    result = sorted([l for l in source_array if l % 2 == 1])
    for index, item in enumerate(source_array):
        if item % 2 == 0:
            result.insert(index, item)
    return result
