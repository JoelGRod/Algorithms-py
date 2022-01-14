import time

""" Countdown
"""

def count_down(value):
    print(value)
    if value <= 0: return           # Base Case
    else: count_down(value - 1)     # Recursive case

print("Countdown\n", "-----------------------")
count_down(10)

""" Search in nested list
"""

def searchItem(test_list, key):
    for item in test_list:
        if item == key: return True                     # Base Case
        if isinstance(item, list):                      # Recursive Case
            if(searchItem(item, key)): return True      
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
print(searchItem(nested_list, "six"))
print(f"{(time.process_time() - start)*1000:8f} ms")

start = time.process_time()
print(search_item_two(nested_list, "six"))
print(f"{(time.process_time() - start)*1000:8f} ms")


""" Search in nested list
"""

def search_item_in_dict(test_dict, key):
    for item in test_dict:
        if test_dict[item] == key: return True                     # Base Case
        if isinstance(test_dict[item], dict):                      # Recursive Case
            if(search_item_in_dict(test_dict[item], key)): return True      
    return False

def search_item_in_dict_two(test_dict, key):
    if test_dict and isinstance(test_dict, dict):
        return any(search_item_in_dict_two(item, key) for item in test_dict.values())
    return test_dict == key

almacen = {
  "estanteria1": {
    "cajon1": {
      "producto1": "coca-cola",
      "producto2": "fanta",
      "producto3": "sprite",
    },
  },
  "estanteria2": {
    "cajon1": "vacio",
    "cajon2": {
      "producto1": "pantalones",
      "producto2": "camiseta",
    },
  },
}
print("-----------------------\n", "Search In dictionary\n", "-----------------------")
start = time.process_time()
print(search_item_in_dict(almacen, "camiseta"))
print(f"{(time.process_time() - start)*1000:8f} ms")

start = time.process_time()
print(search_item_in_dict_two(almacen, "camiseta"))
print(f"{(time.process_time() - start)*1000:8f} ms")