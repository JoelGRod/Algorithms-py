import time

""" Find Highest number in List
"""

def find_highest(numbers):
    if numbers == []: return 0                              # Base Case
    number = find_highest(numbers[1:])                      # Recursive Case
    return numbers[0] if numbers[0] > number else number

# Faster
def find_highest_two(numbers):
    if len(numbers) == 2: return numbers[0] if numbers[0] > numbers[1] else numbers[1]  # Base Case
    number = find_highest_two(numbers[1:])                                              # Recursive Case
    return numbers[0] if numbers[0] > number else number

numbers = [34, 56, 78, 32, 12, 789, 45, 67, 45, 98]


start = time.process_time()
print(find_highest(numbers))
print(f"{(time.process_time() - start)*1000:8f} ms")

start = time.process_time()
print(find_highest_two(numbers))
print(f"{(time.process_time() - start)*1000:8f} ms")