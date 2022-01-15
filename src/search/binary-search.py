import time

""" Binary Search
    O(log n)
    Only on ordered lists
"""

def binary_search(numbers, value):
    lower = 0
    higher = len(numbers) - 1

    while lower <= higher:
        middle = int((lower + higher) / 2)
        estimate = numbers[middle]
        if estimate == value:
            return middle
        if estimate > value:
            higher = middle - 1
        else:
            lower = middle + 1
    return None


def binary_search_recursive(numbers, value):
    middle = int((len(numbers) - 1) / 2)
    if numbers[middle] == value: return True
    if len(numbers) == 1 and numbers[0] != value: return False
    if len(numbers) == 1 and numbers[0] == value: return True

    return (
        binary_search_recursive(numbers[0:middle], value) 
        if value < numbers[middle] 
        else binary_search_recursive(numbers[middle + 1:], value)
    )


numbers = [1, 3, 4, 6, 7, 9, 12, 14, 16, 18, 20, 24, 28, 36, 45, 56]
value = 56

# Binary Search
start = time.process_time()
print("Normal: ", binary_search(numbers, value))
print(f"{(time.process_time() - start)*1000:8f} ms")

# Binary Search Recursive
start = time.process_time()
print("Recursive: ", binary_search_recursive(numbers, value))
print(f"{(time.process_time() - start)*1000:8f} ms")







