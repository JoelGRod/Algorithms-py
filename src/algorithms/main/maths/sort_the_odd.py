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