import time

""" Binary Search
"""

def binary_search_recursive(numbers, value):
    if len(numbers) == 1 and numbers[0] != value: return False
    if len(numbers) == 1 and numbers[0] == value: return True

    middle = int((len(numbers) - 1) / 2)
    if numbers[middle] == value: return True
    return binary_search_recursive(numbers[0:middle], value) if value < numbers[middle] else binary_search_recursive(numbers[middle + 1:], value)


numbers = [1, 3, 4, 6, 7, 9, 12, 14, 16, 18, 20, 24, 28, 36, 45, 56]

start = time.process_time()
print(binary_search_recursive(numbers, 20))
print(f"{(time.process_time() - start)*1000:8f} ms")