import time

""" Search in nested Dict
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