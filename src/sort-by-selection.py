""" O(n^2)
    Slow sort
    Parameters:
        list
        sort type: 
            0 ascendant 
            1 descendant
"""

def find_minor(list):
    minor = list[0]
    minor_idx = 0

    for i in range(1, len(list)):
        if list[i] < minor:
            minor = list[i]
            minor_idx = i
     
    return minor_idx

def find_higher(list):
    higher = list[0]
    higher_idx = 0

    for i in range(1, len(list)):
        if list[i] > higher:
            higher = list[i]
            higher_idx = i
     
    return higher_idx

def sort_by_selection(list, sort_type):
    new_list = []

    for i in range(0, len(list)):
        lower = find_minor(list) if sort_type == 0 else find_higher(list)
        new_list.append(list.pop(lower))
    
    return new_list

test_list = [34, 23, 45, 12, 89, 67, 32, 145, 987, 876, 657, 1001, 2000, 1992, 1982]
print(sort_by_selection(test_list[:], 0))
print(sort_by_selection(test_list[:], 1))
print(test_list)



