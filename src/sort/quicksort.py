import time

""" O(n log n)
    numbers: numbers list
    sort_method:
        0: ascendant
        1: descendant
"""

def quicksort_one(numbers, sort_method):
    if(len(numbers) < 2): return numbers            # Base Case
    elif sort_method == 0:
        pivot = numbers[0]
        lower = [number for number in numbers[1:] if number <= pivot]
        higher = [number for number in numbers[1:] if number > pivot]
        return quicksort(lower, sort_method) + [pivot] + quicksort(higher, sort_method)
    elif sort_method == 1:
        pivot = numbers[0]
        lower = [number for number in numbers[1:] if number <= pivot]
        higher = [number for number in numbers[1:] if number > pivot]
        return quicksort(higher, sort_method) + [pivot] + quicksort(lower, sort_method)

def quicksort(numbers, sort_method):
    if(len(numbers) < 2): return numbers            # Base Case
    else:
        pivot = numbers[0]
        lower = [number for number in numbers[1:] if number <= pivot]
        higher = [number for number in numbers[1:] if number > pivot]
        return (
            quicksort(lower, sort_method) + [pivot] + quicksort(higher, sort_method)
            if sort_method == 0
            else quicksort(higher, sort_method) + [pivot] + quicksort(lower, sort_method)
        )
    
numbers = [6, 7, 1, 56, 878, 675, 987, 2500, 1600, 2800, 234, 456, 789, 675, 56]

start = time.process_time()
print(quicksort(numbers[:], 0))
print(f"{(time.process_time() - start)*1000:8f} ms")

start = time.process_time()
print(quicksort(numbers[:], 1))
print(f"{(time.process_time() - start)*1000:8f} ms")


