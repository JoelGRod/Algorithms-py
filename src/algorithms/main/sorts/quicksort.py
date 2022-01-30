""" 
Quicksort 

A divide and conquer algorithm. Quicksort first divides a large array into 
two smaller sub-arrays: the low elements and the high elements. 
Quicksort can then recursively sort the sub-arrays

The steps are:
    Pick an element, called a pivot, from the array.
    
    Partitioning: reorder the array so that all elements with values less 
    than the pivot come before the pivot, while all elements with values 
    greater than the pivot come after it (equal values can go either way). 
    After this partitioning, the pivot is in its final position. 
    This is called the partition operation.
    
    Recursively apply the above steps to the sub-array of elements with 
    smaller values and separately to the sub-array of elements with greater values.

Best	    Average	    Worst
n log(n)	n log(n)	n2
    
numbers: numbers list
sort_method:
    0: ascendant
    1: descendant
"""

import time

# BAD - Numbers
def quicksort_one(numbers, sort_method):
    if(len(numbers) < 2): return numbers            # Base Case
    elif sort_method == 0:
        pivot = numbers[0]
        lower = [number for number in numbers[1:] if number <= pivot]
        higher = [number for number in numbers[1:] if number > pivot]
        return quicksort_one(lower, sort_method) + [pivot] + quicksort_one(higher, sort_method)
    elif sort_method == 1:
        pivot = numbers[0]
        lower = [number for number in numbers[1:] if number <= pivot]
        higher = [number for number in numbers[1:] if number > pivot]
        return quicksort_one(higher, sort_method) + [pivot] + quicksort_one(lower, sort_method)

# Numbers
def quicksort_numbers(numbers, sort_method):
    if(len(numbers) < 2): return numbers            # Base Case
    else:
        pivot = numbers[0]
        lower = [number for number in numbers[1:] if number <= pivot]
        higher = [number for number in numbers[1:] if number > pivot]
        return (
            quicksort_numbers(lower, sort_method) + [pivot] + quicksort_numbers(higher, sort_method)
            if sort_method == 0
            else quicksort_numbers(higher, sort_method) + [pivot] + quicksort_numbers(lower, sort_method)
        )

# Strings
def quicksort_strings(words, sort_method):
    if(len(words) < 2): return words            # Base Case
    else:
        pivot = words[0]
        lower = [word for word in words[1:] if word.lower() <= pivot.lower()]
        higher = [word for word in words[1:] if word.lower() > pivot.lower()]
        return (
            quicksort_strings(lower, sort_method) + [pivot] + quicksort_strings(higher, sort_method)
            if sort_method == 0
            else quicksort_strings(higher, sort_method) + [pivot] + quicksort_strings(lower, sort_method)
        )

# Better - Global
def quicksort(to_sort, sort_method):
    if(len(to_sort) < 2): return to_sort            # Base Case
    else:
        pivot = to_sort[0]
        lower = (
            [word for word in to_sort[1:] if word.lower() <= pivot.lower()] 
            if isinstance(pivot, str) 
            else [el for el in to_sort[1:] if el <= pivot]
        )
        higher = (
            [word for word in to_sort[1:] if word.lower() > pivot.lower()] 
            if isinstance(pivot, str)
            else [el for el in to_sort[1:] if el > pivot]
        )
        return (
            quicksort(lower, sort_method) + [pivot] + quicksort(higher, sort_method)
            if sort_method == 0
            else quicksort(higher, sort_method) + [pivot] + quicksort(lower, sort_method)
        )
    
numbers = [6, 7, 1, 56, 878, 675, 987, 2500, 1600, 2800, 234, 456, 789, 675, 56]
words = ["Daniel", "dani", "Joel", "Begoña", "Barcelona", "Enzo", "elefante", "Maria", "Rinoceronte", "reino"]

print("Sorting Numbers ascendant")
start = time.process_time()
print(quicksort_numbers(numbers[:], 0))
print(f"{(time.process_time() - start)*1000:8f} ms")

print("Sorting Numbers descendant")
start = time.process_time()
print(quicksort_numbers(numbers[:], 1))
print(f"{(time.process_time() - start)*1000:8f} ms")

print("Sorting Strings ascendant")
start = time.process_time()
print(quicksort_strings(words[:], 0))
print(f"{(time.process_time() - start)*1000:8f} ms")

print("Sorting Strings descendant")
start = time.process_time()
print(quicksort_strings(words[:], 1))
print(f"{(time.process_time() - start)*1000:8f} ms")

print("Sorting Strings ascendant - Global Quicksort")
start = time.process_time()
print(quicksort(words[:], 0))
print(f"{(time.process_time() - start)*1000:8f} ms")

print("Sorting Strings descendant - Global Quicksort")
start = time.process_time()
print(quicksort(words[:], 1))
print(f"{(time.process_time() - start)*1000:8f} ms")

print("Sorting Numbers ascendant - Global Quicksort")
start = time.process_time()
print(quicksort(numbers[:], 0))
print(f"{(time.process_time() - start)*1000:8f} ms")

print("Sorting Numbers descendant - Global Quicksort")
start = time.process_time()
print(quicksort(numbers[:], 1))
print(f"{(time.process_time() - start)*1000:8f} ms")

print("Sorting Strings ascendant - list.sort()")
start = time.process_time()
words.sort(key = lambda word: word.lower())
print(words)
print(f"{(time.process_time() - start)*1000:8f} ms")

print("Sorting Strings descendant - list.sort()")
start = time.process_time()
words.sort(key = lambda word: word.lower(), reverse = True)
print(words)
print(f"{(time.process_time() - start)*1000:8f} ms")

print("Sorting Strings ascendant - sorted()")
start = time.process_time()
print(sorted(words, key = lambda word: word.lower()))
print(f"{(time.process_time() - start)*1000:8f} ms")

print("Sorting Strings descendant - sorted()")
start = time.process_time()
print(sorted(words, key = lambda word: word.lower(), reverse = True))
print(f"{(time.process_time() - start)*1000:8f} ms")


