import time

""" Search in nested list
"""

def search_item(test_list, key):
    for item in test_list:
        if item == key: return True                     # Base Case
        if isinstance(item, list):                      # Recursive Case
            if(search_item(item, key)): return True      
    return False

def search_item_two(test_list, key):
    if test_list and isinstance(test_list, list):
        return any(search_item_two(item, key) for item in test_list)
    return test_list == key

nested_list = [
    ["1", "2", "3", 
        ["one", "two", 
            ["three", "four"]
        ]
    ],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["10", "11", "12"],
    ["13", "14", "15"],
    ["16", "17", "18",
        ["five", "six"]
    ],
    "thing"
]

print("-----------------------\n", "Search In List\n", "-----------------------")
start = time.process_time()
print(search_item(nested_list, "six"))
print(f"{(time.process_time() - start)*1000:8f} ms")

start = time.process_time()
print(search_item_two(nested_list, "six"))
print(f"{(time.process_time() - start)*1000:8f} ms")