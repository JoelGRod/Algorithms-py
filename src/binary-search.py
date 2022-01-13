""" O(log n)
    Only on ordered lists
"""

test_list = [1, 3, 4, 6, 7, 9, 12, 14, 16, 18, 20, 24, 28, 36, 45, 56]

def binary_search(list, value):
    lower = 0
    higher = len(list) - 1

    while lower <= higher:
        middle = int((lower + higher) / 2)
        estimate = list[middle]
        if estimate == value:
            return middle
        if estimate > value:
            higher = middle - 1
        else:
            lower = middle + 1
    return None

print(binary_search(test_list, 25))





